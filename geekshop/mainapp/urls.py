from django.urls import path
import mainapp.views as mainapp

import adminapp.views.product_views as product_views

app_name = 'mainapp'

urlpatterns = [
    path('', product_views.products, name='index'),
    path('category/<int:pk>/', product_views.products, name='category'),
    path('category/<int:pk>/page/<int:page>/', mainapp.products, name='page'),
    path('product/<int:pk>/', mainapp.product, name='product'),
]
