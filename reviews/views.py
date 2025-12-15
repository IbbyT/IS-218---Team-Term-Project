from django.shortcuts import render, redirect
from reviews.forms import ReviewsForm
from reviews.models import Feedback

def review(request):
    form = ReviewsForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("review")

    all_reviews = Feedback.objects.all().select_related('product').order_by('-id')

    context = {
        "form": form,
        "reviews": all_reviews,
    }
    
    return render(request, "reviews/review.html", context) 


def contact(request):
    return render(request, "reviews/contact.html")