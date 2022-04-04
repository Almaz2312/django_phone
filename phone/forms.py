from django import forms
from .models import Phone


class PhoneCreateForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = "__all__"


class SearchForm(forms.Form):
    text = forms.CharField(label='Search by product name', max_length=250)
