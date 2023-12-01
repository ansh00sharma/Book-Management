from django.urls import path
from . import views

urlpatterns = [
    path('user_register', views.user_register, name="register user"),
    path('user_login', views.user_login, name="login user"),
    path('add_books', views.add_books, name="add_books"),
    path('show_Dbcollection', views.show_Dbcollection, name="show_Dbcollection"),
]