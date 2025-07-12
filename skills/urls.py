from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_skill, name='add_skill'),
    path('browse/', views.browse_skills, name='browse_skills'),
]
