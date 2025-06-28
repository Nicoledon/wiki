from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:headline>" , views.page , name = "page")
]
