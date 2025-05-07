from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BookForm
from .models import Book
from django.db.models import Q


@login_required
def create_book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            book.save()
            return redirect('home')  # Redirige a donde prefieras
    else:
        form = BookForm()
    return render(request, 'books/create_book.html', {'form': form})

@login_required
def my_books_view(request):
    books = Book.objects.filter(owner=request.user)
    return render(request, 'books/my_books.html', {'books': books})


def exchange_books_view(request):
    city_filter = request.GET.get('city', '')
    author_filter = request.GET.get('author', '')

    books = Book.objects.exclude(owner=request.user)

    if city_filter:
        books = books.filter(location__icontains=city_filter)
    if author_filter:
        books = books.filter(author__icontains=author_filter)

    # Obtener valores únicos
    cities = Book.objects.exclude(owner=request.user).values_list('location', flat=True).distinct()
    authors = Book.objects.exclude(owner=request.user).values_list('author', flat=True).distinct()

    return render(request, 'books/exchange_books.html', {
        'books': books,
        'cities': sorted(set(cities)),
        'authors': sorted(set(authors)),
        'selected_city': city_filter,
        'selected_author': author_filter
    })
