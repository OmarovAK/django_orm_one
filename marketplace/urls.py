"""marketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from library.views import list_books, filter_date
from phonemarket.views import all_phones, phone_detail, list_pages

urlpatterns = [
    path('admin/', admin.site.urls),
    path('phones/', all_phones, name='phones'),
    path('phones/<slug:slug>/', phone_detail, name='detail_phone'),
    path('', list_pages, name='home'),
    path('library/', list_books, name='list_books'),
    path('library/<str:date_>', filter_date, name='filter_date_books')
]
