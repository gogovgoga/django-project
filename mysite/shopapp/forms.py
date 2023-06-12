from django import forms
from django.contrib.auth.models import Group
from multiupload.fields import MultiFileField
from shopapp.models import Product, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "price", "description", "discount", "preview", "images"

    images = MultiFileField(min_num=1, max_num=10)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = 'delivery_address', 'promo_code', 'user', 'products'


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name"]


