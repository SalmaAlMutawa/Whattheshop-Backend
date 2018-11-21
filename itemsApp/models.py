from django.db import models

class Item(models.Model):
	name = models.CharField(max_length=120)
	category = models.CharField(max_length=120)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.ImageField(upload_to='item_pics', null=True, blank=True)

