# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('signin/', views.signin_view, name='signin'),
    path('dashboard/', views.dashboard_view, name='dashboard'),  # Add this line
    path('manage_ipo/', views.manage_ipo, name='manage_ipo'),
    path('register_ipo/', views.register_ipo, name='register_ipo'),
    path('userside_ipo/', views.userside_ipo, name='userside_ipo'),
]
