from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('skill/toggle/<int:skill_id>/', views.toggle_skill_approval, name='toggle_skill_approval'),
    path('user/toggle/<int:user_id>/', views.toggle_user_ban, name='toggle_user_ban'),
    path('broadcast/', views.broadcast_message, name='broadcast_message'),
    path('export/', views.export_data_csv, name='export_data_csv'),
]
