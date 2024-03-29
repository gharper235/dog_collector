from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
POTTY = (
    ('0', 'N/A'),
    ('1', 'Pee'),
    ('2', 'Poo'),
    ('3', 'Both')
)


class Food(models.Model):
    name = models.CharField(max_length=50)
    flavor = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=250, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('food_detail', kwargs={'food_id': self.id})


class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    foods = models.ManyToManyField(Food)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})


class Walking(models.Model):
    date = models.DateField('walk date')
    time = models.TimeField(auto_now=False, auto_now_add=False,)
    potty = models.CharField(
        max_length=1,
        choices=POTTY,
        default=POTTY[0][0]
    )
    # Create a dog_id FK
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_potty_display()} on {self.date}"

    class Meta:
        ordering = ['-date']


class Photo(models.Model):
    url = models.CharField(max_length=200)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for _id: {self.dog_id} @{self.url}"
