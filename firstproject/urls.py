from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('', views.testpaper, name='home'),   # 👈 Home route added
    path('admin/', admin.site.urls),
    path('testpaper/', views.testpaper),
]
