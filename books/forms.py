from django import forms
from .models import Book, ExchangeRequest

BOOK_CONDITIONS = [
    ('nuevo', 'Nuevo'),
    ('casi_nuevo', 'Casi nuevo'),
    ('bueno', 'Usado en buen estado'),
    ('aceptable', 'Con señales de uso'),
    ('deteriorado', 'Deteriorado o dañado'),
]

class BookForm(forms.ModelForm):
    condition = forms.ChoiceField(choices=BOOK_CONDITIONS, label="Condición del libro")

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'condition', 'location']

    def clean_location(self):
        location = self.cleaned_data['location']
        return location.strip().lower()  # 🔍 Limpia espacios y convierte a minúsculas

class ExchangeRequestForm(forms.ModelForm):
    offered_book = forms.ModelChoiceField(
        queryset=Book.objects.none(),  # Se definirá dinámicamente en la vista
        label='Selecciona un libro tuyo para ofertar',
        required=True
    )

    class Meta:
        model = ExchangeRequest
        fields = ['offered_book']

class FastRatingForm(forms.Form):
    score = forms.ChoiceField(
        choices=[(i, f'{i} ★') for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
