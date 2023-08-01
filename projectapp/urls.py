from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    # path('navbar/', views.navbar),
    # path('punce/', views.punce),
    # path('remove/', views.remove_punce),
    path("checkthumb/", views.slide),
    path("noname/", views.home1, name="noname"),
]