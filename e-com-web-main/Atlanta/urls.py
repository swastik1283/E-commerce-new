"""
URL configuration for hashmi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from hashmi import views
from django.contrib.auth import views as auth_views
from . form import loginform 

urlpatterns = [
    path('',views.home , name="home"),
    path('admin/', admin.site.urls),
    path('catagory/<slug:val>', views.catagory, name="catagory" ),
    path('product_detail/<slug:slug1>', views.product_detail, name="product_detail" ),
    path('about/', views.about, name="about" ),
    path('contact/', views.contact, name="contact" ),
    path('registration/', views.registration, name="registration" ),
    path('login/', views.loginf , name="login" ),
    path('profile/', views.profile, name="profile" ),
    path('address/', views.address, name="address" ),
    path('updateaddress/<int:pk>', views.updateaddress.as_view(), name="updateaddress" ),
    path('password_reset_1/',views.password_reset_1 , name='password_reset_1'),
    path('logout/',auth_views.LogoutView.as_view(next_page = 'login') , name="logout"),

    path('add_to_cart/',views.add_to_cart , name='add_to_cart'),
    path('cart/',views.showcart , name='showcart'),
    path('checkout/',views.checkout , name='checkout'),
    path('pluscart/',views.plus_cart ),
    path('minuscart/',views.minus_cart ),
    path('removecart/',views.remove_cart ),


]

urlpatterns += static(settings.MEDIA_RUL,document_root = settings.MEDIA_ROOT)

