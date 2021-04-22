from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import uuid
import boto3
from .models import Dog, Food, Photo
from .forms import WalkingForm

# Add these "constants" below the imports
S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'ghcatcollector'

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


def add_photo(request, dog_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to dog_id or dog (if you have a dog object)
            photo = Photo(url=url, dog_id=dog_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', dog_id=dog_id)
