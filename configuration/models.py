from django.db import models
from landing.models import client
from products.models import *

class config(models.Model):
    #login = models.ForeignKey(client, blank=True, null=True, default=None)
    CPU = models.ForeignKey(CPU, blank=True, null=False, default=None, on_delete=models.CASCADE)
    Motherboard = models.ForeignKey(Motherboard, blank=True, null=True, default=None, on_delete=models.CASCADE)
    RAM = models.ForeignKey(RAM, blank=True, null=True, default=None, on_delete=models.CASCADE)
    Graphic_adapter = models.ForeignKey(GPU, blank=True, null=True, default=None, on_delete=models.CASCADE)
    Power_supply = models.ForeignKey(Power_supply, blank=True, null=True, default=None, on_delete=models.CASCADE)
    HDD = models.ForeignKey(HDD, blank=True, null=True, default=None, on_delete=models.CASCADE)
    SSD = models.ForeignKey(SSD, blank=True, null=True, default=None, on_delete=models.CASCADE)
    Case = models.ForeignKey(case, blank=True, null=True, default=None, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s %s %s %s" % (self.id, self.CPU, self.Graphic_adapter, self.Motherboard)

    class Meta:
        verbose_name = 'Конфигурация'
        verbose_name_plural = 'Конфигурации'