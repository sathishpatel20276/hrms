from django.urls import path
from . import views

urlpatterns = [
    path('',views.home ),
    path("register/", views.register, name='register'),
    path("login/", views.login, name='login'),
    path("logout/", views.logout, name='logout'),
    path("register/login/", views.login, name='login'),
    path("search/", views.searchbar, name='search'),
    path("profile/", views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
    path("leave_request/",views.leave_request),
    path("leave_status/",views.leave_status),

]
