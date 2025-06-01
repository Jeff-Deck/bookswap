from django.db import models
from users.models import CustomUser

class Book(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Propietario")
    title = models.CharField(max_length=255, verbose_name="Título")
    author = models.CharField(max_length=255, verbose_name="Autor")
    genre = models.CharField(max_length=100, verbose_name="Género")
    condition = models.CharField(max_length=100, verbose_name="Condición")
    location = models.CharField(max_length=255, verbose_name="Ubicación")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    available = models.BooleanField(default=True, verbose_name="Disponible")


    def __str__(self):
        return self.title

class ExchangeRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('accepted', 'Aceptado'),
        ('rejected', 'Rechazado'),
    ]

    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_requests')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='exchange_requests')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Solicitud de {self.sender} a {self.receiver} por "{self.book}" ({self.status})'


class ExchangeHistory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='exchanges_sent')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='exchanges_received')
    exchanged_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.book.title} de {self.sender} a {self.receiver} el {self.exchanged_on}"

