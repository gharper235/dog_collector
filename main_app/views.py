from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dog
from .forms import WalkingForm

# Create your views here.

# Define the home view


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})


def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    walking_form = WalkingForm()
    return render(request, 'dogs/detail.html', {'dog': dog, 'walking_form': walking_form})


def add_walking(request, dog_id):
    form = WalkingForm(request.POST)
    print(form.errors)
    if form.is_valid():
        new_walking = form.save(commit=False)
        new_walking.dog_id = dog_id
        new_walking.save()
    return redirect('detail', dog_id=dog_id)


class DogCreate(CreateView):
    model = Dog
    fields = '__all__'


class DogUpdate(UpdateView):
    model = Dog
    # Disallow the renaming of a dog by excluding the name field!
    fields = ['breed', 'description', 'age']


class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'
