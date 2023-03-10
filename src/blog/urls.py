from django.urls import path

from .views import *

urlpatterns = [
    path('category/<str:slug>/', get_category, name='category'),
    path('post/<str:slug>/', get_post, name='post'),
    path('', Home.as_view(), name='index'),
]
