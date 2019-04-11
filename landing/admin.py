from django.contrib import admin
from .models import *

class client_ext(admin.ModelAdmin):
    list_display = [field.name for field in client._meta.fields]


    class Meta:
        model = client

admin.site.register(client, client_ext)
