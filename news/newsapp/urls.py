"""news URL Configuration

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

from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name = 'home'),
    path('sport/', views.sports , name = 'sport'),
    path('entertainment/', views.entertainment , name = 'entertainment'),
    path('health/', views.health , name = 'health'),
    path('sensex/',views.sensex,name='sensex'),
    path('technology/', views.technology , name = 'technology'),
    path('business/', views.business , name = 'business'),
    path('politics/', views.politics , name = 'politics'),
    path('literature/', views.literature , name = 'literature'),
    path('corona/', views.corona , name = 'corona'),
    path('about/', views.about , name = 'about'),
]
