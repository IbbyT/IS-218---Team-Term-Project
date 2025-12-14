from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request, "products/home.html")    

def product_list(request):
    return HttpResponse("Product list page (pies, cakes, sweets...)")

def product_detail(request, pk):
    return HttpResponse(f"Product detail page for product #{pk}")