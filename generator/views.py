from django.shortcuts import render, redirect
import random
from .models import PasswordSafe
from django.contrib import messages

# Create your views here.
def home(request):
	return render(request, 'about.html')

def password(request):
	return render(request, 'home.html')

def generator(request):
	if request.method == 'POST':
		user = request.POST['user']
		Password = request.POST['passw']

		creater = PasswordSafe(platform = user, Password= Password)
		creater.save()
		messages.info(request, 'Your password is saved to the database!!')
		return render(request, 'Thankyou.html')
		
	else:
		characters = list('abcdefghijklmnopqrstuvwxyz')
		length = int(request.GET.get('length',8))

		if request.GET.get('uppercase'):
			characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

		if request.GET.get('numbers'):
			characters.extend(list('0123456789'))

		if request.GET.get('specialChar'):
			characters.extend(list('!@#$%^&*()+-?<>][}|{'))

		password=''

		for i in range(length):
			password += random.choice(characters)

		print(password)
		return render(request, 'generator.html', {'password':password})