from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.contrib.auth.views import LoginView, LogoutView

from mysite import settings
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', include('scorestore.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
