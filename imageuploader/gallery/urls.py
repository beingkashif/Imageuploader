from django.urls import path
from . import views

urlpatterns=[
    path('pdlist/', views.product_list, name='producg_list'),
    path('', views.home, name = 'home')
]