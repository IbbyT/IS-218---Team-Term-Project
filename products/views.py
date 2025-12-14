from django.shortcuts import render
from django.http import HttpResponse
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


# PRODUCT DETAIL PAGE (placeholder for now)
def product_detail(request, pk):
	return HttpResponse(f"Product detail page for product #{pk}")
