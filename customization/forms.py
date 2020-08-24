from .models import coffee_file
from django import forms
import io, csv


class CoffeeForm(forms.ModelForm):
    class Meta:
        model = coffee_file
        fields = ('csv_file',)
