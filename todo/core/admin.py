from django.contrib import admin
from .models import *
# Register your models here.
@admin.register((Task))
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','completed']
