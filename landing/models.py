from django.db import models

class client(models.Model):
    login = models.CharField(max_length=30)
    email = models.EmailField()
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.login
