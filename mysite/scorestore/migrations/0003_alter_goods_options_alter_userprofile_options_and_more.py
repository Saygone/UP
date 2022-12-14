# Generated by Django 4.0.5 on 2022-06-23 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scorestore', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goods',
            options={'verbose_name': 'Товары', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Данные пользователей', 'verbose_name_plural': 'Данные пользователей'},
        ),
        migrations.AlterField(
            model_name='goods',
            name='count',
            field=models.IntegerField(default=5, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Публикация'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.IntegerField(default=5, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время создания'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='time_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Время обновления'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='points',
            field=models.IntegerField(default=100, verbose_name='Кол-во очков'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='telegramID',
            field=models.CharField(blank=True, max_length=9, verbose_name='Телеграм'),
        ),
    ]
