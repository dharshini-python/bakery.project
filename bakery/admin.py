from django.contrib import admin
from .models import Category, Product , Topcategory

# Register your models here.
admin.site.register(Topcategory)
admin.site.register(Category)
admin.site.register(Product)