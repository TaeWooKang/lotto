from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('form', views.post),
    path('detail', views.detail, name='detail'),
    path(
        'detail/<int:num>/<str:text>',
        views.detail2, name='detail2'
    ),
    path('join', views.join, name='join'),
    path('id_check', views.id_check, name='id_check'),
]