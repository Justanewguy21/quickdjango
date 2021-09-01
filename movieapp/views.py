from django.http import response
from django.shortcuts import render
# Create a home page views here.
# this is the home page of movieapp
def home(request):
    return render(request, 'home.html', {})
