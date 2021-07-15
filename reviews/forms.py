from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user_profile', 'product',)

    review_rating = forms.IntegerField(
        label='Rating: 1 - 5',
        widget=forms.NumberInput(
            attrs={'min': 1, 'max': 5, 'class': 'text-center'})
        )
