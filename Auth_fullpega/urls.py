from django.urls import path
from Registro_fullpega import views
from Auth_fullpega import views

urlpatterns = [
    path('login', views.auth_login, name="auth_login"),
    path('logout', views.auth_logout, name="auth_logout"),
    path('restablecer_contrasenha', views.restablecer_contrasenha, name="restablecer_contrasenha"),
    # path('restablecer_contrasenha_mensaje', views.restablecer_contrasenha_mensaje, name="restablecer_contrasenha_mensaje"),
]
