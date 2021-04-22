from django.contrib import admin
from .models import Dog, Walking, Food

# import your models here
from .models import Dog

# Register your models here
admin.site.register(Dog)
admin.site.register(Walking)
admin.site.register(Food)
