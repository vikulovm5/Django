from django.urls import path
from .views import basket, basket_add, basket_remove

app_name = 'basketapp'

urlpatterns = [
    path('view/', basket, name='view'),
    path('add/<int:pk>', basket_add, name='add'),
    path('remove/', basket_remove, name='remove'),
]