from django import forms 
from .models import Testimonial

class TestimonioForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'comment', 'rating', 'photo']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Share your experience...'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }