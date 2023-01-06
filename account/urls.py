
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login_page'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('users/', views.users, name='users'),
]
