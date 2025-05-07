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

    def __str__(self):
        return self.title
