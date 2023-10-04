
from django import forms

from hw4_store_app.models import Product


class ImageForm(forms.Form):
    image = forms.ImageField()

class ProductUpd(forms.Form):
    product = forms.ModelChoiceField(label='Product', empty_label='Please select',
                                     queryset=Product.objects.all(),
                                     widget=forms.Select(attrs={'class': 'form-control'}))
    product_name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    image = forms.ImageField()