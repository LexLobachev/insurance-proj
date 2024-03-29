from io import BytesIO
from PIL import Image
from django.core.files import File
from main.settings import STATIC_URL

from django.db import models
from vendor.models import Vendor


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=55)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, related_name="products", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=55)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    added_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)

    class Meta:
        ordering = ['-added_date']

    def __str__(self):
        return self.title

    def get_thumbnail(self):
        if self.thumbnail:
            return f'{STATIC_URL}{self.thumbnail}'
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return f'{STATIC_URL}{self.thumbnail}'

            else:
                return 'https://via.placeholder.com/240x180.jpg'

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail