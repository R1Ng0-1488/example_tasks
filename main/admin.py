from django.contrib import admin
from .models import Task, CSVFile

admin.site.register(Task)
admin.site.register(CSVFile)
