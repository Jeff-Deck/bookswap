from django import forms
from .models import Book, ExchangeRequest

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'condition', 'location']

class ExchangeRequestForm(forms.ModelForm):
    class Meta:
        model = ExchangeRequest
        fields = ['book']

class FastRatingForm(forms.Form):
    score = forms.ChoiceField(
        choices=[(i, f'{i} ★') for i in range(1, 6)],
        widget=forms.RadioSelect
    )
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
