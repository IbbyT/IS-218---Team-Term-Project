from django.shortcuts import render
from django.shortcuts import redirect
from reviews.forms import ReviewsForm

# Create your views here.
def contact(request):
    return render(request, "reviews/contact.html" ) 

def review(request):
    form = ReviewsForm(request.POST or None)
        
    if request.method == "POST":
        if form.is_valid():
            form.save
            return redirect("home")
    else:
        return render(request, "reviews/review.html", {"form": form})