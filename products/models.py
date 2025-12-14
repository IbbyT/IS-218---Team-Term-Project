from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.core.validators import FileExtensionValidator
import uuid
import os

def product_upload_path(_, filename):
	ext = filename.split('.')[-1]
	new_filename = f"{uuid.uuid4()}.{ext}"
	return os.path.join('products', new_filename)

class Product(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.FileField(
		upload_to=product_upload_path,
		validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
	)

	def __str__(self):
		return self.name

@receiver(post_delete, sender=Product)
def cleanup_product_image(sender, instance, **kwargs):
	if instance.image:
		if os.path.isfile(instance.image.path):
			os.remove(instance.image.path)

from django.db.models.signals import pre_save

@receiver(pre_save, sender=Product)
def cleanup_product_image(sender, instance, **kwargs):
	if not instance.pk:
		return  # new product, nothing to delete

	try:
		old_image = Product.objects.get(pk=instance.pk).image
	except Product.DoesNotExist:
		return

	new_image = instance.image
	if old_image and old_image != new_image:
		if os.path.isfile(old_image.path):
			os.remove(old_image.path)
