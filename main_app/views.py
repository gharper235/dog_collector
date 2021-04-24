from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
import uuid
import boto3
from .models import Dog, Food, Photo
from .forms import WalkingForm

from decouple import config

# Add these "constants" below the imports
S3_BASE_URL = config('S3_BASE_URL')
BUCKET = config('BUCKET')

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
    fields = ['name', 'breed', 'description', 'age']

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)


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


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
