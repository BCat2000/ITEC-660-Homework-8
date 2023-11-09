# Go to mycontactsapp open **admin.py** add the following code:

# Register your models here.
from .models import Contact
from django.contrib import admin


admin.site.register(Contact)