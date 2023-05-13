from django.db import models
from django.shortcuts import render


class Car(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    available = models.IntegerField(default=0)
    image = models.CharField(max_length=1000, blank=True, default=())
    price = models.IntegerField(default=0)

    def car_left(self) -> int:
        ordered = Order.objects.filter(car=self).count()
        purchased = Purchase.objects.filter(car=self).count()
        return purchased - ordered

    def __str__(self):
        return f"{self.id}: {self.name}, available:{self.available}"


class Name(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    age = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}, Age:{self.age}"


class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=100, default="created")

    def __str__(self):
        return f"{self.id}: {self.car}, {self.name}, phone:{self.phone,} " \
               f"{self.status}"


#Поступление машин в салон
class Purchase(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    datetime = models.DateField(auto_now_add=True)
    count = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.car} purchase on date:{self.datetime}"


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    credit_card = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.order}, amount: {self.amount} date: " \
               f"{self.date}"
