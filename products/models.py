from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="Descripción pendiente")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()

    def __str__(self):
        return self.name

    @property
    def secure_image_url(self):
        if self.image_url and self.image_url.startswith("http://"):
            return self.image_url.replace("http://", "https://")
        return self.image_url
