from django.contrib import admin
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import userProfile

class userProfileAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('id', 'avatar')  # оставляем только имя и цену товара
    # list_filter = ('dateCreation', 'author')  # добавляем примитивные фильтры в нашу админку
    # search_fields = ('title', 'text')  # тут всё очень похоже на фильтры из запросов в базу
    # actions = [nullfy_rating]  # добавляем действия в список


admin.site.register(userProfile, userProfileAdmin)

