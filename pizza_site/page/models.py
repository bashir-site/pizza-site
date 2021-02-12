from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField('Изображение', upload_to='pizza/')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Лучшее предложение'
        verbose_name_plural = 'Лучшие преложения'
    

class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Menu(models.Model):
    name = models.CharField('Название', max_length=40)
    description = models.TextField('Описание')
    image = models.ImageField("Изображение", upload_to='menu/', height_field=None, width_field=None, max_length=None)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey("Category", verbose_name="Категория", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


    