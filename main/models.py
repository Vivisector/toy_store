from django.db import models

# Create your models here.
class Buyer(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=20)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.username

class Game(models.Model):
    title = models.CharField(max_length=100)  # Название игры
    description = models.TextField()  # Описание игры
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Стоимость игры
    # release_date = models.DateField()  # Дата выпуска игры (по желанию)

    def __str__(self):
        return self.title

