
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),  # ecom
    path('addtoshopcart/<int:id>', views.addtoshopcart, name='addtoshopcart'),
    path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),

]