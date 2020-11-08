from django.urls import path
from . import views

urlpatterns = [

    path('user/',views.register),
    path('user/index', views.index),
    path('user/index/a', views.a),
    path('user/index/b', views.b),

]