from django.contrib import admin
from .models import *


class CPU_admin (admin.ModelAdmin):
    list_display = [field.name for field in CPU._meta.fields]

    class Meta:
        model = CPU

admin.site.register(CPU, CPU_admin)

class Motherboard_admin (admin.ModelAdmin):
    list_display = [field.name for field in Motherboard._meta.fields]

    class Meta:
        model = Motherboard

admin.site.register(Motherboard, Motherboard_admin)

class RAM_admin (admin.ModelAdmin):
    list_display = [field.name for field in RAM._meta.fields]

    class Meta:
        model = RAM

admin.site.register(RAM, RAM_admin)

class GPU_admin (admin.ModelAdmin):
    list_display = [field.name for field in GPU._meta.fields]

    class Meta:
        model = GPU

#admin.site.register(GPU, GPU_admin)

class Power_supply_admin (admin.ModelAdmin):
    list_display = [field.name for field in Power_supply._meta.fields]

    class Meta:
        model = Power_supply

admin.site.register(Power_supply, Power_supply_admin)

class GPU_admin (admin.ModelAdmin):
    list_display = [field.name for field in GPU._meta.fields]

    class Meta:
        model = GPU

admin.site.register(GPU, GPU_admin)

class HDD_admin (admin.ModelAdmin):
    list_display = [field.name for field in HDD._meta.fields]

    class Meta:
        model = HDD

admin.site.register(HDD, HDD_admin)

class SSD_admin (admin.ModelAdmin):
    list_display = [field.name for field in SSD._meta.fields]

    class Meta:
        model = SSD

admin.site.register(SSD, SSD_admin)

class Case_admin (admin.ModelAdmin):
    list_display = [field.name for field in case._meta.fields]

    class Meta:
        model = case

admin.site.register(case, Case_admin)



