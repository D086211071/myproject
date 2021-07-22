"""vijay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('water/', views.index, name='water'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name="login"),
    path('water/date',views.dara,name='dara'),
    path('today/date',views.dara,name='dara'),
    path('water/new/', views.newpatient, name='new'),
    path('today/', views.today, name='today'),
    path('water/superuserd/',views.superuserd),
    path('water/water', views.index),
    path('water/new/edit/<int:id>',views.edit),
    path('water/new/edit/update/',views.update),
    path('water/old/',views.old,name='old'),
    path('water/old/dest/<int:id>',views.dele,name='des'),
    path('back/',views.back,name='bak'),
]
