from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('user/<int:user_id>/', views.view_profile, name='view_profile'),

]
