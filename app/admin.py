from django.contrib import admin
from .models import Result,File,Bill    

# Register your models here.
admin.site.register(Result)
admin.site.register(File)
admin.site.register(Bill)