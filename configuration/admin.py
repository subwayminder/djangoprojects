from django.contrib import admin
from .models import *


class config_admin (admin.ModelAdmin):
    list_display = [field.name for field in config._meta.fields]

    class Meta:
        model = config

admin.site.register(config, config_admin)