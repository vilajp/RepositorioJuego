"""juego URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.partida import views
from apps.registro.forms import RegistroFormulario
from apps.registro import views as registro
from apps.estadisticas import views as view_estadistica
from apps.administrador import views as view_admin
from django.contrib.auth import views as auth

#BOOTSTRAP IMPORT
from apps.bootstrap import views as view_bootstrap

urlpatterns = [
    path("",view_bootstrap.principal,name='principal' ),
    path("home/",views.home,name='home' ),
    path('borrar/', views.borrar, name = "borrar"),
    path('creo-juego/', views.creo_juego, name = "creo-juego"),
    path('admin/', admin.site.urls),
    path('administrador/',view_admin.admin,name="administrador"),
    path('partida/',views.comienzo,name="partida"),
    path('registro/', registro.register, name = 'registro' ),
    path('login/',auth.LoginView.as_view(template_name = 'login.html'),name = 'login'),
    path('logout/',auth.LogoutView.as_view(),name = 'logout'),
    path('estadistica/',view_estadistica.estadistica, name = 'estadistica'),
    path('resultados/',view_estadistica.resultados_juego, name = 'resultados'),
    path("postales/",view_bootstrap.postales,name='postales' ),
    path("equipo/",view_bootstrap.equipo,name='equipo'),
    path("masinfo/",view_bootstrap.masinfo,name='masinfo'),
    path("contacto/",view_bootstrap.contacto,name='contacto'),
    path("detalle-portfolio/",view_bootstrap.detalle_portfolio,name='portfolio'),



    #path("home/",views.home,name='home' ),



]
