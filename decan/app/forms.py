from django import forms


class AddProduct(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    price = forms.IntegerField()
