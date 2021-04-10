from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm
from django.contrib import messages

class ProductView(View):
	def get(self,request):
		topwears=Product.objects.filter(category='TW')
		bottomwears=Product.objects.filter(category='BW')
		mobiles=Product.objects.filter(category='M')
		context={
		'topwears':topwears,
		'bottomwears':bottomwears,
		'mobiles':mobiles
		}
		return render(request,'app/home.html',context)
		

class ProductDetailView(View):
	def get(self,request,pk):
		product=Product.objects.get(pk=pk)
		context={'product':product}
		return render (request, 'app/productdetail.html',context)

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request,data=None):
	if data==None:
		mobiles=Product.objects.filter(category='M')
	elif data=='Redmi' or data=='Samsung':
		mobiles=Product.objects.filter(category='M').filter(brand=data)
		
	return render(request,'app/mobile.html',{'mobiles':mobiles})


class CustomerRegistrationView(View):
	def get(self, request):
		form=CustomerRegistrationForm()
		return render(request,'app/customerregistration.html',{'form':form})
	def post(self,request):
		form=CustomerRegistrationForm(request.POST)
		if form.is_valid():
			messages.success(request,'Congratulations ! Registration Sucessful')
			form.save()
		return render(request,'app/customerregistration.html',{'form':form})




def checkout(request):
 return render(request, 'app/checkout.html')
