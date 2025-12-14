#takes the model data from reviews
#and turns it into forms

from django import forms
from reviews.models import Feedback

class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["product", "rating", "comment"]