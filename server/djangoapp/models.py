from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    SEDAN = 'Sedan'
    SUV = 'SUV'
    WAGON = 'Wagon'
    HATCHBACK = 'Hatchback'
    TRUCK = 'Truck'
    CAR_TYPES = [
        (SEDAN, 'Sedan'), (SUV, 'SUV'), (WAGON, 'Wagon'),
        (HATCHBACK, 'Hatchback'), (TRUCK, 'Truck'),
    ]
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=CAR_TYPES, default=SEDAN)
    year = models.IntegerField(default=2023, validators=[MaxValueValidator(2023), MinValueValidator(2015)])
    dealer_id = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.car_make.name} {self.name}"