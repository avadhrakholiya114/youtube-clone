from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("video/<int:id>", views.detail, name="video"),

    path('save_comment/', views.save_comment, name='save_comment'),

]
