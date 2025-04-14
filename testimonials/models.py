from django.db import models

class Testimonial(models.Model):
    name = models.CharField("Nombre", max_length=100)
    comment = models.TextField("Comentario")
    rating = models.IntegerField("Calificación (1 a 5)", default=5)
    photo = models.ImageField("Foto del cliente", upload_to='testimonials/', blank=True, null=True)
    created_at = models.DateTimeField("Fecha de publicación", auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.rating}⭐) - {self.comment[:30]}..."