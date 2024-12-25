from django.db import models


# Create your models here.
class Buyer(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.username


class Game(models.Model):
    title = models.CharField(max_length=100)  # Название игры
    description = models.TextField()  # Описание игры
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Стоимость игры
    size = models.IntegerField(default=0)

    # release_date = models.DateField()  # Дата выпуска игры (по желанию)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=100)  # Название овости
    content = models.TextField()  # Описание игры
    pub_date = models.DateTimeField(auto_now_add=True)  # Дата размещения

    class Meta:
        verbose_name = "Новость"  # Название в единственном числе
        verbose_name_plural = "Новости"  # Название во множественном числе

    def __str__(self):
        return self.title
