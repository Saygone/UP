from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .forms import *
from .models import *

menu = [
    {'title': "Войти", 'url_name': 'login'},
    {'title': "Магазин", 'url_name': 'shop'},
    {'title': "Личный кабинет", 'url_name': 'profile'},
    {'title': "Дополнительно", 'url_name': 'operations'},
    {'title': "Выйти", 'url_name': 'logout'},
]


# Вывод шаблона shop.html с созданными продуктами
def shop(request):
    posts = Goods.objects.all()
    return render(request, 'scorestore/shop.html', {'posts': posts, 'menu': menu, 'title': 'Магазин', })

# Вывод всех пользователей на шаблоне allusers.html
def allusers(request):
    users = User.objects.all()
    userprofiles = UserProfile.objects.all()
    return render(request, 'scorestore/allusers.html',
                  {'users': users, 'userprofiles': userprofiles, 'menu': menu, 'title': 'Список пользователей', })

# Добавление предмета
def additem(request):
    # Проверка на запрос
    if request.method == 'POST':
        form = AddItemForm(request.POST, request.FILES)
        # Проверка формы на валидность
        if form.is_valid():
            form.save()
            return redirect('shop')
    else:
        form = AddItemForm()
    return render(request, 'scorestore/additem.html', {'form': form, 'menu': menu, 'title': 'Добавление товара'})

# Вывод шаблона profile.html с личным кабинетом пользователя
def profile(request):
    return render(request, 'scorestore/profile.html', {'menu': menu, 'title': 'Профиль'})

# Вывод шаблона operations.html со специальными возможностями пользователя
def operations(request):
    return render(request, 'scorestore/operations.html', {'menu': menu, 'title': 'Операции'})

# Вывод шаблона login.html с авторизацией пользователя
def login_(request):
    return render(request, 'scorestore/login.html', {'menu': menu, 'title': 'Вход'})

# Добавление нового пользователя
def register(request):
    # Проверка на запрос
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        # Проверка формы на валидность
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            # Сохранение пользователя в бд
            profile.save()
            # Очистка полей и переход на страницу operations
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            return redirect('operations')

    else:
        # Добавление дополнительной формы к изначальной
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {'form': form, 'profile_form': profile_form, 'menu': menu}
    return render(request, 'scorestore/register.html', context)

# Заказ и списание баллов
def order(request, post_id):
    post = get_object_or_404(Goods, pk=post_id)
    user = User.objects.get(id=request.user.id)

    # Получение id и points текущего пользователя
    current_user_points = user.userprofile.points
    current_user_id = request.user.id

    user_points = current_user_points
    price_of_item = post.price

    # Переменная для обработки списания баллов у пользователя
    alpha = user_points - price_of_item

    if alpha < 0:
        messages.info(request, 'У вас недостаточно очков на счету')

    else:
        UserProfile.objects.filter(id=current_user_id).update(points=alpha)
        return redirect('shop')

    context = {
        'post': post,
        'menu': menu,
        'title': post.name,
    }
    return render(request, 'scorestore/post.html', context=context)


