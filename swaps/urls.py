from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:receiver_id>/', views.create_swap, name='create_swap'),
    path('dashboard/', views.swap_dashboard, name='swap_dashboard'),
    path('update/<int:swap_id>/<str:status>/', views.update_swap_status, name='update_swap_status'),
    path('cancel/<int:swap_id>/', views.cancel_swap, name='cancel_swap'),
]
