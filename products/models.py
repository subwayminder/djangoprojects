from django.db import models

class CPU(models.Model):
    product_name = models.CharField(max_length=70, blank=True, null=True, default=None)
    product_type = models.CharField(max_length=20, blank=True, null=True, default=None)
    cores = models.IntegerField(max_length=3, blank=True, null=True, default=None)
    threads = models.IntegerField(max_length=3, blank=True, null=True, default=None)
    socket = models.CharField(max_length=20, blank=True, null=True, default=None)
    L3_cache = models.CharField(max_length=10, blank=True, null=True, default=None)
    bit_depth = models.IntegerField(max_length=3, blank=True, null=True, default=None)
    base_frequency = models.CharField(max_length=10, blank=True, null=True, default=None)
    TDP = models.IntegerField(max_length=10, blank=True, null=True, default=None)
    memory_type = models.CharField(max_length=20, blank=True, null=True, default=None)
    num_mem_channels = models.IntegerField(max_length=3, blank=True, null=True, default=None)
    unlocked_multiplier = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s %s %s" % (self.id, self.product_name, self.socket)

    class Meta:
        verbose_name = 'Процессор'
        verbose_name_plural = 'Процессоры'

class Motherboard(models.Model):
    product_name = models.CharField(max_length=70, blank=True, null=True, default=None)
    product_type = models.CharField(max_length=20, blank=True, null=True, default=None)
    vendor = models.CharField(max_length=20, blank=True, null=True, default=None)
    socket = models.CharField(max_length=20, blank=True, null=True, default=None)
    chipset = models.CharField(max_length=30, blank=True, null=True, default=None)
    memory_form = models.CharField(max_length=20, blank=True, null=True, default=None)
    numb_mem_slots = models.IntegerField(max_length=2, blank=True, null=True, default=None)
    usb3 = models.BooleanField()
    usb_type_C = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s %s %s %s" % (self.id, self.product_name, self.socket, self.chipset)

    class Meta:
        verbose_name = 'Материнская плата'
        verbose_name_plural = 'Материнские платы'

class RAM(models.Model):
    product_name = models.CharField(max_length=70, blank=True, null=True, default=None)
    product_type = models.CharField(max_length=20, blank=True, null=True, default=None)
    vendor = models.CharField(max_length=20, blank=True, null=True, default=None)
    memory_type = models.CharField(max_length=20, blank=True, null=True, default=None)
    memory_form = models.CharField(max_length=20, blank=True, null=True, default=None)
    memory_size = models.CharField(max_length=20, blank=True, null=True, default=None)
    speed = models.CharField(max_length=20, blank=True, null=True, default=None)
    latency = models.CharField(max_length=20, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s %s %s %s" % (self.id, self.product_name, self.memory_type, self.memory_size)

    class Meta:
        verbose_name = 'Модуль памяти'
        verbose_name_plural = 'Модули памяти'

class GPU(models.Model):
    product_name = models.CharField(max_length=70, blank=True, null=True, default=None)
    product_type = models.CharField(max_length=20, blank=True, null=True, default=None)
    vendor = models.CharField(max_length=20, blank=True, null=True, default=None)
    GPU_designer = models.CharField(max_length=20, blank=True, null=True, default=None)
    interface = models.CharField(max_length=20, blank=True, null=True, default=None)
    GPU_speed = models.CharField(max_length=15, blank=True, null=True, default=None)
    GPU_memtype = models.CharField(max_length=15, blank=True, null=True, default=None)
    GPU_memsize = models.CharField(max_length=15, blank=True, null=True, default=None)
    power_usage = models.CharField(max_length=15, blank=True, null=True, default=None)
    VGA = models.BooleanField()
    DVI = models.BooleanField()
    HDMI = models.BooleanField()
    Display_port = models.BooleanField()
    SLI_or_crossfire = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s %s %s %s" % (self.id, self.product_name, self.interface, self.vendor)

    class Meta:
        verbose_name = 'Видеокарта'
        verbose_name_plural = 'Видеокарты'

class Power_supply(models.Model):
    product_name = models.CharField(max_length=70, blank=True, null=True, default=None)
    product_type = models.CharField(max_length=20, blank=True, null=True, default=None)
    manufacturer = models.CharField(max_length=20, blank=True, null=True, default=None)
    power = models.CharField(max_length=15, blank=True, null=True, default=None)
    form_factor = models.CharField(max_length=15, blank=True, null=True, default=None)
    molex = models.IntegerField(max_length=3, blank=True, null=True, default=None)
    sata = models.IntegerField(max_length=3, blank=True, null=True, default=None)
    mb_cpu_supply = models.CharField(max_length=20, blank=True, null=True, default=None)
    Graphic_adapter_supply = models.CharField(max_length=20, blank=True, null=True, default=None)
    module_or_semi_module = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s %s %s %s" % (self.id, self.product_name, self.form_factor, self.power)

    class Meta:
        verbose_name = 'Блок питания'
        verbose_name_plural = 'Блоки питания'

class HDD(models.Model):
    product_name = models.CharField(max_length=70, blank=True, null=True, default=None)
    product_type = models.CharField(max_length=20, blank=True, null=True, default=None)
    capacity = models.CharField(max_length=20, blank=True, null=True, default=None)
    spin_speed = models.CharField(max_length=20, blank=True, null=True, default=None)
    form_factor = models.CharField(max_length=15, blank=True, null=True, default=None)
    fail_time = models.CharField(max_length=15, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s %s %s %s" % (self.id, self.product_name, self.capacity, self.spin_speed)

    class Meta:
        verbose_name = 'Жесткий диск'
        verbose_name_plural = 'Жесткие диски'

class SSD(models.Model):
    product_name = models.CharField(max_length=70, blank=True, null=True, default=None)
    product_type = models.CharField(max_length=20, blank=True, null=True, default=None)
    capacity = models.CharField(max_length=20, blank=True, null=True, default=None)
    memory_type = models.CharField(max_length=20, blank=True, null=True, default=None)
    interface = models.CharField(max_length=20, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s %s %s %s %s" % (self.id, self.product_name, self.capacity, self.memory_type, self.interface)

    class Meta:
        verbose_name = 'Твердотельный накопитель'
        verbose_name_plural = 'Твердотельные накопители'

class case(models.Model):
    product_name = models.CharField(max_length=70, blank=True, null=True, default=None)
    product_type = models.CharField(max_length=20, blank=True, null=True, default=None)
    brand = models.CharField(max_length=20, blank=True, null=True, default=None)
    form_factor = models.CharField(max_length=20, blank=True, null=True, default=None)
    built_in_powersupply = models.BooleanField()
    power = models.CharField(max_length=20, blank=True, null=True, default=None)
    audio_in_out = models.BooleanField()
    usb_2_front = models.IntegerField(max_length=2, blank=True, null=True, default=None)
    usb_3_front = models.IntegerField(max_length=2, blank=True, null=True, default=None)
    graphic_adapter_size = models.IntegerField(max_length=2, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s %s %s %s" % (self.id, self.product_name, self.brand, self.form_factor)

    class Meta:
        verbose_name = 'Корпус'
        verbose_name_plural = 'Корпусы для ПК'