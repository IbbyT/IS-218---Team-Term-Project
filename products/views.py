from django.shortcuts import render, get_object_or_404
from .models import Product

# HOME PAGE
def home(request):
	return render(request, "products/home.html")


# PRODUCTS LIST PAGE
def product_list(request):
	products = Product.objects.all()
	return render(request, "products/product_list.html", {
		"products": products
	})


# PRODUCT DETAIL PAGE
def product_detail(request, id):
	product = get_object_or_404(Product, id=id)
	return render(request, "products/product_detail.html", {
		"product": product
	})
