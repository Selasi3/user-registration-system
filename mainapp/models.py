from itertools import count
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    other_names = models.CharField(max_length=100, null=True, blank=True)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    number = models.CharField(validators=[phoneNumberRegex], max_length=17)
    email = models.EmailField(max_length=100)
    time_registered = models.DateTimeField(default= timezone.now)
    Gender =(("M","Male" ),("F","Female"))
    gender = models.CharField(max_length=1, choices=Gender, blank=False)


    class Meta:
        unique_together = ['first_name', 'last_name','number', 'gender']



    def __str__(self):
        return f"{self.first_name} , {self.last_name}"

 