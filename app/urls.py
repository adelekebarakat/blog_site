from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.login, name='login'),
    # dynamic urls
    path('product/<str:num>', views.product, name='product')

]
