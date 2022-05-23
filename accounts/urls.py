from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.login, name='index_login'),
    path('login/',views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

