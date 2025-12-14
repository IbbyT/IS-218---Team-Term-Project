from django.shortcuts import render
from django.http import HttpResponse


# HOME PAGE
def home(request):
    return render(request, "products/home.html")


# PRODUCTS LIST PAGE
def product_list(request):
    return render(request, "products/product_list.html")


# PRODUCT DETAIL PAGE (placeholder for now)
def product_detail(request, pk):
    return HttpResponse(f"Product detail page for product #{pk}")