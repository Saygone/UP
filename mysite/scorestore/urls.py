from django.urls import path
from .views import *

urlpatterns = [
    path('shop', shop, name='shop'),
    path('profile/', profile, name='profile'),
    path('operations/', operations, name='operations'),
    path('register/', register, name='register'),
    path('post/<int:post_id>/', order, name='post'),
    path('allusers/', allusers, name='allusers'),
    path('additem/', additem, name='additem'),
]