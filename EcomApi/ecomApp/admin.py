from django.contrib import admin

# Register your models here.
from .models import Book,Category,Product

admin.site.register(Book)
admin.site.register(Product)
admin.site.register(Category)