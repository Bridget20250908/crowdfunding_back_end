from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.CustomUserlist.as_view()),
    path('users/<int:pk>/', views.CustomUserDetail.as_view())
]
