from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Модифицируем пользователя
class UserProfile(models.Model):
    # Подключаем таблицу 1:1 к оригинальной таблице пользователи
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Добавляем поле points содержащее количество очков пользователя
    points = models.IntegerField(default=100,
                                 verbose_name="Кол-во очков")
    # Добавляем поле telegramID содержащее идентификатор телеграма пользователя
    telegramID = models.CharField(max_length=9,
                                  blank=True,
                                  verbose_name="Телеграм")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Данные пользователей'
        verbose_name_plural = 'Данные пользователей'

# Создаем класс для продукта
class Goods(models.Model):
    # Наименование продукта
    name = models.CharField(max_length=255,
                            verbose_name="Наименование")
    # Описание продукта
    description = models.TextField(blank=True,
                                   verbose_name="Описание")
    # Цена продукта
    price = models.IntegerField(default=5,
                                verbose_name="Цена")
    # Количество продукта
    count = models.IntegerField(default=5,
                                verbose_name="Количество")
    # Фото продукта
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/",
                              verbose_name="Фото")
    # Время когда продукт был создан
    time_create = models.DateTimeField(auto_now_add=True,
                                       verbose_name="Время создания")
    # Время когда продукт был обновлен
    time_update = models.DateTimeField(auto_now=True,
                                       verbose_name="Время обновления")
    # Опубликован ли продукт
    is_published = models.BooleanField(default=True,
                                       verbose_name="Публикация")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'