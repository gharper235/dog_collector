from django.db import models
from django.urls import reverse

# Create your models here.
POTTY = (
    ('0', 'N/A'),
    ('1', 'Pee'),
    ('2', 'Poo'),
    ('3', 'Both')
)


class Food(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    # Other goodness such as 'def __str__():' below
    def __str__(self):
        return f'{self.name} {self.color}'

    # Add this method
    def get_absolute_url(self):
        return reverse('food_detail', kwargs={'food_id': self.id})

        class Meta:
            ordering = ['-date']


class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()

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
