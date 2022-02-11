from django.forms import ModelForm

from product.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'description', 'interest_rate']
