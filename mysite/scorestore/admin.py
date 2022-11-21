from django.contrib import admin
from .models import *

# Обновление модели класса Goods в панели администратора для последующих изменений
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'id')

# Регистрация класса пользователь в панели администратора для последующих изменений
admin.site.register(UserProfile)

# Регистрация класса Goods и GoodsAdmin в панели администратора для последующих изменений
admin.site.register(Goods, GoodsAdmin)
