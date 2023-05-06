from django.db import models

# Create your models here.


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.booking_date}"


class MenuItem(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return self.title

    def get_item(self):
        return f'{self.title} : {str(self.price)}'
