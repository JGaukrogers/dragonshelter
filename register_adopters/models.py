from django.core import validators
from django.db import models


class AdoptersCharacteristic(models.Model):
    characteristic_name = models.CharField(max_length=50, unique=True)
    characteristic_description = models.CharField(max_length=500)

    def __str__(self):
        return self.characteristic_name


class Adopter(models.Model):
    adopters_name = models.CharField(max_length=50)
    id_number = models.IntegerField(unique=True, validators=[validators.MinValueValidator(1000), validators.MaxValueValidator(99999999)])
    date_of_birth = models.DateField()

    list_of_characteristics = models.ManyToManyField(AdoptersCharacteristic, blank=True)

    def __str__(self):
        return self.adopters_name