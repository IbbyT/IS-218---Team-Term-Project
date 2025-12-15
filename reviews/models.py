from django.db import models
from products.models import Product
from django.core.validators import MinValueValidator, MaxValueValidator

class Feedback(models.Model):
	username = models.CharField(max_length=150, default='Anonymous')
	product = models.ForeignKey(
		Product,
		on_delete=models.CASCADE,
		related_name='feedbacks'
	)
	rating = models.PositiveSmallIntegerField(
		validators=[MinValueValidator(1), MaxValueValidator(10)]
	)
	comment = models.TextField()

	def __str__(self):
		return f"{self.product.name} - {self.rating}"
