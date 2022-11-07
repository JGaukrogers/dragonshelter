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

    def get_age(self) -> int:
        today = date.today()
        year_diff = today.year - self.birthdate.year
        birthdate_to_come = 1
        if today.month > self.birthdate.month:
            birthdate_to_come = 0
        elif today.month == self.birthdate.month:
            if today.day >= self.birthdate.day:
                birthdate_to_come = 0

        return year_diff - birthdate_to_come

    def __str__(self):
        return self.name
