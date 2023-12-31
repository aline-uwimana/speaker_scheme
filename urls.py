from django.urls import path
from . import views

urlpatterns = [
    path("", views.read),
    path("insert/", views.insert),
    path("update/", views.update),
    path("delete/", views.delete),
]
