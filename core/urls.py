from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("video/<int:id>", views.detail, name="video"),

    # comment
    path('save_comment/', views.save_comment, name='save_comment'),
    path('delete_comment/', views.delete_comment, name='delete_comment'),

    # subscriber

    path('new_subsciber/<int:id>/', views.new_subscriber, name='new_subsciber'),
    path('load_sub/<int:id>/', views.load_sub, name='load_sub')
]
