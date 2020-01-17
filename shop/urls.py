from django.contrib import admin
from django.urls import path, include, register_converter

from shop import views
from shop.converters import FourDigitYearConverter

register_converter(FourDigitYearConverter, 'yyyy')

app_name = 'shop'

urlpatterns = [
    path('archives/<yyyy:year>/', views.archives_year),
    path('', views.item_list)
]