from django.shortcuts import render
from django.http import HttpResponse
from .dog_class import dogs

# Create your views here.

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
def about(request):
  return render(request, 'about.html')
def dogs_index(request):
  return render(request, 'dogs/index.html', { 'dogs': dogs })