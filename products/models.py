from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="Descripción pendiente")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()

    def __str__(self):
        return self.name

