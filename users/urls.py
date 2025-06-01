from django.urls import path
from .views import register_view, login_view, logout_view, ver_perfil_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('<int:user_id>/', ver_perfil_view, name='ver_perfil'),


]
