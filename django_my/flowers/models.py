from django.db import models

class Articles(models.Model):
    name = models.CharField("Название", max_length=55)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='media/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f"Название: {self.name}"
