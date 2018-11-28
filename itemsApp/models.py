from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

class Item(models.Model):
	name = models.CharField(max_length=120)
	category = models.CharField(max_length=120)
	description = models.TextField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.ImageField(upload_to='item_pics', null=True, blank=True)

	def __str__(self):
		return self.name

class Address(models.Model):
	# user= models.ForeignKey(User, on_delete=models.CASCADE)
	name=models.CharField(max_length=120, default='home')
	area= models.CharField(max_length=120)
	block = models.PositiveIntegerField(default=1)
	avenue=models.CharField(max_length=200, null=True, blank=True)
	street = models.CharField(max_length=200)
	house = models.PositiveIntegerField(default=1)
	extra_instructions = models.CharField(max_length=120, null=True, blank=True)

	def __str__(self):
		return self.name

class Order(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	date=models.DateField(auto_now_add=True)
	# address=models.ForeignKey(Address, on_delete=models.CASCADE)



class MiddleMan(models.Model):
	item=models.ForeignKey(Item, on_delete=models.CASCADE, related_name="middle_man")
	quantity=models.PositiveIntegerField(default=1)
	order=models.ForeignKey(Order, on_delete=models.CASCADE, related_name="middle_man")

	def __str__(self):
		return self.item.name
