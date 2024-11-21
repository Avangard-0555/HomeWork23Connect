from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('<имя_приложения>.urls')),  # Подключение маршрутов приложения
]
# http://127.0.0.1:8000/about/ — страница "О нас"
# http://127.0.0.1:8000/contact/ — страница "Контакты"
# http://127.0.0.1:8000/services/ — страница "Услуги"
