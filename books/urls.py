from django.urls import path
from .views import (
    create_book_view,
    my_books_view,
    exchange_books_view,
    send_exchange_request,
    received_requests_view,
    handle_request_view,
    exchange_history_view,
    rate_exchange_view
)

urlpatterns = [
    path('crear/', create_book_view, name='create_book'),
    path('mis-libros/', my_books_view, name='my_books'),
    path('intercambiar/', exchange_books_view, name='exchange_books'),
    path('exchange/send/<int:book_id>/', send_exchange_request, name='send_exchange_request'),
    path('solicitudes/', received_requests_view, name='received_requests'),
    path('solicitudes/gestionar/<int:request_id>/', handle_request_view, name='handle_request'),
    path('historial/', exchange_history_view, name='exchange_history'),
    path('historial/calificar/<int:exchange_id>/', rate_exchange_view, name='rate_exchange'),

]
