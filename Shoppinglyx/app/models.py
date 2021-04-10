from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
STATE_CHOICES=(
	('Ghorashal','Ghorashal'),
	('Monohardi','Monohardi'),
	('Shibpur','Shibpur'),
	('Raipura','Raipura'),
	('Madhabdi','Madhabdi'),
	('Mirzapur','Mirzapur'),
	('Dhanbari','Dhanbari'),
	('Madhupur','Madhupur'),
	('Chhagalnaiya','Chhagalnaiya'),
	('Parshuram','Parshuram'),
	('Bandarban','Bandarban'),
	('Rangamati','Rangamati')
	)
class Customer(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	name=models.CharField(max_length=50)
	city=models.CharField(max_length=20)
	zipcode=models.IntegerField()
	state=models.CharField(choices=STATE_CHOICES,max_length=50)

	def __str__(self):
		return str(self.id)

CATEGORY_CHOICES=(
	('M', 'Mobile'),
	('L', 'Laptop'),
	('TW', 'Top Wear'),
	('BW', 'Bottom Wear')
	)
class Product(models.Model):
	title=models.CharField(max_length=50)
	selling_price= models.FloatField()
	discounted_price=models.FloatField()
	description=models.CharField(max_length=200)
	brand=models.CharField(max_length=50)
	category=models.CharField(choices=CATEGORY_CHOICES, max_length=2)
	product_image=models.ImageField(upload_to='productimg')

	def __str__(self):
		return str(self.id)

class Cart(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	quantity=models.PositiveIntegerField(default=1)

	def __str__(self):
		return str(self.id)

STATUS_CHOICES=(
	('Accepted','Accepted'),
	('Packed','Packed'),
	('On The Way','On The Way'),
	('Delivered','Delivered'),
	('Cancel','Cancel')

	)

class OrderPlaced(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	quantity=models.PositiveIntegerField(default=1)
	ordered_date=models.DateTimeField(auto_now_add=True)
	status=models.CharField(max_length=30,choices=STATUS_CHOICES,default='Pending')





