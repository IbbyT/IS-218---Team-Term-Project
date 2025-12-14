from django.urls import path
from .views import review
from .views import contact

urlpatterns = [
    path("reviews/", review, name="review"),
    path("contact/", contact, name="contact"),
    ]