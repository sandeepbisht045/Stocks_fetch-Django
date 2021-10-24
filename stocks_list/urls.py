"""stock_market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),
    path("signup",views.signup,name="signup"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),   
    path("send_otp",views.send_otp,name="send otp"),
    path("logout",views.logout,name="logout"),   
    path("stocks",views.stocks,name="stocks"),
    path("load_data",views.load_data,name="load_data"),
    path("query/<int:id>",views.query,name="query"),
    path("search",views.search,name="search"),
    path("details/<slug>",views.details,name="details"),
    path("export",views.export,name="export"),
    path("admin",views.admin,name="admin")
    
    
    
    
    
       
    
    
]
