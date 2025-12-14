from django.contrib import admin
from .models import Product, Tag

class ProductAdmin(admin.ModelAdmin):
	list_display = ('name',)
	filter_horizontal = ('tags',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Tag)
