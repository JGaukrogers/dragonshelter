from django.db import models
from datetime import date


class DragonType(models.Model):
    type_name = models.CharField(max_length=50)
    characteristics = models.CharField(max_length=500)

    def __str__(self):
        return self.type_name


class Dragon(models.Model):
    name = models.CharField(max_length=50)
    birthdate = models.DateField('birthdate')
    dragon_type = models.ForeignKey(DragonType, on_delete=models.CASCADE)

    def get_age(self):
        diff = date.today() - self.birthdate
        return int(diff.days / 365.25)

    def __str__(self):
        return self.name
