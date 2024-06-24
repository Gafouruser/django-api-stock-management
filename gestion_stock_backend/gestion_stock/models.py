from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name


class Stock(models.Model):
    objects = None
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - Quantity: {self.quantity}"


class Order(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commande de {self.user.username} - Date de création: {self.created_at}"


class OrderItem(models.Model):
    objects = None
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"Commande: {self.order}, Produit: {self.product.name}, Quantité: {self.quantity}"
