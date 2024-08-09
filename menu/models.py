from django.db import models

# Create your models here.


class Coffees(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField()
    is_alcocol = models.BooleanField()

    class Meta:
        verbose_name_plural = 'Кофе'
        verbose_name = 'Кофе'


class Publication(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    created_date = models.DateField()

    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'




class Feedback(models.Model):
    full_name = models.CharField(max_length=120)
    comment = models.TextField(max_length=500)
    avatar = models.ImageField()
    create_date =  models.DateField(null=True)


    class Meta:
        verbose_name_plural = 'Отзывы'
        verbose_name = 'Отзыв'


class MokkoContact(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    email = models.EmailField()
    short_description = models.TextField(null=True)


    class Meta:
        verbose_name_plural = 'Контакты Мокко'
        verbose_name = 'Контакты Мокко'


class ClientContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=25)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Клиент Контакты"
        verbose_name = "Клиент Контакты"


class NameVerbose(models.Model):
    Titlle = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "Названия"
        verbose_name = "Названия"


