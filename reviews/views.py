from django.shortcuts import render, redirect
from reviews.forms import ReviewsForm

def review(request):
    form = ReviewsForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("home")  # or redirect("reviews:review")

    return render(request, "reviews/review.html", {"form": form})


def contact(request):
    return render(request, "reviews/contact.html")