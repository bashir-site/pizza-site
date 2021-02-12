# Generated by Django 3.1.6 on 2021-02-11 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='menu/', verbose_name='Изображение')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
    ]
