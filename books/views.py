from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BookForm,FastRatingForm  
from .models import Book, ExchangeRequest,ExchangeHistory  
from django.db.models import Q
import requests

@login_required
def create_book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'books/create_book.html', {'form': form})

@login_required
def my_books_view(request):
    books = Book.objects.filter(owner=request.user)
    return render(request, 'books/my_books.html', {'books': books})

@login_required
def exchange_books_view(request):
    city_filter = request.GET.get('city', '')
    author_filter = request.GET.get('author', '')

    books = Book.objects.exclude(owner=request.user).filter(available=True)

    if city_filter:
        books = books.filter(location__icontains=city_filter)
    if author_filter:
        books = books.filter(author__icontains=author_filter)

    cities = Book.objects.exclude(owner=request.user).values_list('location', flat=True).distinct()
    authors = Book.objects.exclude(owner=request.user).values_list('author', flat=True).distinct()

    return render(request, 'books/exchange_books.html', {
        'books': books,
        'cities': sorted(set(cities)),
        'authors': sorted(set(authors)),
        'selected_city': city_filter,
        'selected_author': author_filter
    })

@login_required
def send_exchange_request(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.owner == request.user:
        return redirect('home')  # Evita que un usuario solicite su propio libro

    ExchangeRequest.objects.create(
        sender=request.user,
        receiver=book.owner,
        book=book
    )
    return redirect('received_requests')  # <- Corrección importante

@login_required
def received_requests_view(request):
    requests = ExchangeRequest.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'books/received_requests.html', {'requests': requests})

@login_required
def handle_request_view(request, request_id):
    req = get_object_or_404(ExchangeRequest, id=request_id, receiver=request.user)

    if req.status == 'pending' and request.method == 'POST':
        action = request.POST.get('action')
        if action == 'accept':
            req.status = 'accepted'
            req.book.available = False
            req.book.save()

            # Rechazar otras solicitudes pendientes por este libro
            ExchangeRequest.objects.filter(
                book=req.book,
                status='pending'
            ).exclude(id=req.id).update(status='rejected')

            # Registrar en el historial
            ExchangeHistory.objects.create(
                book=req.book,
                sender=req.sender,
                receiver=req.receiver
            )

        elif action == 'reject':
            req.status = 'rejected'

        req.save()
    return redirect('received_requests')

@login_required
def exchange_history_view(request):
    user = request.user
    history = ExchangeHistory.objects.filter(
        Q(sender=user) | Q(receiver=user)
    ).order_by('-exchanged_on')

    rated_exchanges = set()

    try:
        response = requests.get(f"http://localhost:8001/ratings/by-rater/{user.id}")
        if response.status_code == 200:
            rated_data = response.json()
            for rating in rated_data:
                rated_exchanges.add(rating["exchange_id"])
    except Exception as e:
        print("❌ Error al obtener calificaciones hechas por el usuario:", e)

    print("🧪 Intercambios en historial:", [r.id for r in history])
    print("🧪 Ya calificados según FastAPI:", rated_exchanges)

    for record in history:
        record.can_rate = record.id not in rated_exchanges

    return render(request, 'books/exchange_history.html', {'history': history})



@login_required
def rate_exchange_view(request, exchange_id):
    exchange = get_object_or_404(ExchangeHistory, id=exchange_id)
    user = request.user
    other_user = exchange.receiver if user == exchange.sender else exchange.sender

    # Verificar si el usuario actual ya calificó este intercambio
    try:
        response = requests.get(f"http://localhost:8001/ratings/user/{user.id}")
        if response.status_code == 200:
            for r in response.json():
                if r["exchange_id"] == exchange.id and r["rater_id"] == user.id:
                    return redirect('exchange_history')  # Ya calificó este intercambio
    except Exception as e:
        print("Error al verificar si ya calificó:", e)

    if user not in [exchange.sender, exchange.receiver]:
        return redirect('exchange_history')

    if request.method == 'POST':
        form = FastRatingForm(request.POST)
        if form.is_valid():
            data = {
                "exchange_id": exchange.id,
                "rated_user_id": other_user.id,
                "rater_id": user.id,  # ⬅️ nuevo campo obligatorio
                "score": int(form.cleaned_data['score']),
                "comment": form.cleaned_data['comment']
            }
            try:
                response = requests.post("http://localhost:8001/ratings/", json=data)
                if response.status_code == 200:
                    return redirect('exchange_history')
            except Exception as e:
                print("Error al guardar la calificación en FastAPI:", e)
    else:
        form = FastRatingForm()

    return render(request, 'books/rate_exchange.html', {
        'form': form,
        'exchange': exchange,
        'other_user': other_user
    })
