from django.db import models
import datetime
# Create your models here.
from django.core.validators import MinValueValidator,MaxValueValidator

class Category(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Customer(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=40)
    price = models.DecimalField(default=0, decimal_places=0, max_digits=12)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    picture = models.ImageField(upload_to='upload/product')

    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=0, max_digits=12)

    star = models.IntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.is_sale:
            if self.sale_price <= 0:
                # Set the sale_price to price if it is not provided or invalid
                self.sale_price = self.price
            elif self.sale_price > self.price:
                # Ensure sale_price is not greater than the original price
                self.sale_price = self.price
        else:
            # Reset sale_price to 0 if is_sale is False
            self.sale_price = 0

        super(Product, self).save(*args, **kwargs)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(default='', blank=False, max_length=400)
    phone = models.CharField( blank=True, max_length=20)
    date = models.DateTimeField(default=datetime.datetime.today())
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name