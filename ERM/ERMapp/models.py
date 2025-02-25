from django.db import models

# Create your models here.


class Customer(models.Model):
    customerCode = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    orderNumber = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.customerCode} - {self.name} - {self.orderNumber}"


class Item(models.Model):
    itemCode = models.AutoField(primary_key=True)
    itemName = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    unitPrice = models.FloatField(max_length=255)
    stock = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.itemCode} - {self.itemName} - {self.description} - {self.unitPrice} - {self.stock}"


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customerCode = models.CharField(max_length=255, null=True)
    customerName = models.CharField(max_length=255, null=True)
    customerOrderNumber = models.CharField(max_length=255, null=True)
    customerOrderDate = models.CharField(max_length=255, null=True)
    itemCode = models.IntegerField(null=True)
    itemName = models.CharField(max_length=255)
    quantity = models.IntegerField(null=True)
    unitPrice = models.FloatField(max_length=255)
    stock = models.IntegerField(null=True)
    total = models.FloatField(max_length=255)

    def __str__(self):
        return f"{self.id} - {self.customerCode} - {self.customerName} - {self.customerOrderNumber} - {self.customerOrderDate} - {self.itemCode} - {self.itemName} - {self.quantity} - {self.unitPrice} - {self.stock} - {self.total}"