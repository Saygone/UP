from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

# Форма для регистрации нового пользователя
class ExtendedUserCreationForm(UserCreationForm):
    # Поле для электронной почты
    email = forms.EmailField()
    # Поле для имени
    first_name = forms.CharField(max_length=30)
    # Поле для фамилии
    last_name = forms.CharField(max_length=150)

    # Собственно форма с данными
    class Meta:
        # Использующаяся модель = User
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

# Дополнительная форма для регистрации
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = 'telegramID'

# Форма для авторизации
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# Форма для добавления предмета на витрину
class AddItemForm(forms.ModelForm):
    class Meta:
        # Модель использующаяся в форме = Goods
        model = Goods
        # Поля из модели использующиеся в форме
        fields = ['name', 'price', 'count', 'photo', 'is_published']


