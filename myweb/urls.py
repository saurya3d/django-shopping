"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from ecom import views
from order import views as OrderViews
from user import views as UserViews

urlpatterns = [
    path('', include('ecom.urls')),
    path('product/', include('product.urls')),
    path('order/', include('order.urls')),
    path('ecom/', include('ecom.urls')),
    path('user/', include('user.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),


    path('contact/', views.contactus, name='contactus'),
    path('search/', views.search, name='search'),
    path('search_auto/', views.search_auto, name='search_auto'),
    path('category/<int:id>/<slug:slug>', views.category_products, name='category_products'),
    path('product/<int:id>/<slug:slug>', views.product_detail, name='product_detail'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('shopcart/', OrderViews.shopcart, name='shopcart'),
    path('signup/', UserViews.signup_form, name='signup_form'),
    path('login/', UserViews.login_form, name='login_form'),
    path('logout/', UserViews.logout_func, name='logout_func'),
    path('faq/', UserViews.faq, name='faq'),
    path('ajaxcolor/', views.ajaxcolor, name='ajaxcolor')


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
