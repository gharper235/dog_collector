from django.contrib import admin
from .models import Dog, Walking

# import your models here
from .models import Dog

# Register your models here
admin.site.register(Dog)
admin.site.register(Walking)
