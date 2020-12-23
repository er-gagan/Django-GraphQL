from django.contrib import admin
from .models import Person,User
# Register your models here.
admin.site.register((Person,User))