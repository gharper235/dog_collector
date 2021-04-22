from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dog, Food
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
    foods_dog_doesnt_have = Food.objects.exclude(
        id__in=dog.foods.all().values_list('id'))
    walking_form = WalkingForm()
    return render(request, 'dogs/detail.html', {'dog': dog, 'walking_form': walking_form, 'foods': foods_dog_doesnt_have})


def add_walking(request, dog_id):
    form = WalkingForm(request.POST)
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

# Food views


def foods_index(request):
    foods = Food.objects.all()
    context = {
        'foods': foods
    }
    return render(request, 'foods/index.html', context)


def food_detail(request, food_id):
    food = Food.objects.get(id=food_id)
    context = {
        'food': food
    }
    return render(request, 'foods/detail.html', context)


class Create_Food(CreateView):
    model = Food
    fields = '__all__'


class Update_food(UpdateView):
    model = Food
    fields = ['flavor', 'description']


class Delete_food(DeleteView):
    model = Food
    success_url = '/foods/'


def remove_food(request, dog_id, food_id):
    Dog.objects.get(id=dog_id).foods.remove(food_id)
    return redirect('detail', dog_id=dog_id)


def assoc_food(request, dog_id, food_id):
    # Note that you can pass a food's id instead of the whole object
    Dog.objects.get(id=dog_id).foods.add(food_id)
    return redirect('detail', dog_id=dog_id)
