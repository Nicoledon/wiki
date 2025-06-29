from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("page/<str:headline>" , views.page , name = "page"),
    path("modify",views.modify,name = "modify"),
    path("edit/<str:elem>" , views.edit , name = "edit"),
    path("random",views.randoms, name = "random")
]
