"""login_crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from reg import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Sign_up, name='signup'),
    path('login/', views.User_login, name='login'),
    path('profile/', views.User_profile, name='profile'),
    path('logout/', views.User_logout, name='logout'),
    path('updatedata/<int:id>/', views.Update_data, name='updatedata'),
    path('delete/<int:id>/', views.Delete_data, name='deletedata'),
    path('customer/', views.Customers, name='customer'),
    path('viewdata/<int:id>', views.View_data, name='viewdata'),
    path('customerall/<int:id>', views.Customers_all, name='viewdata_all'),
    

]
