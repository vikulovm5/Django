import adminapp.views as adminapp
from django.urls import path

import adminapp.views.user_views as user
import adminapp.views.category_views as category
import adminapp.views.product_views as product

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', user.user_create, name='user_create'),
    path('users/read/', user.UsersListView.as_view(), name='users'),
    path('users/update/<int:pk>/', user.user_update, name='user_update'),
    path('users/delete/<int:pk>/', user.user_delete, name='user_delete'),



    path('categories/create/', category.ProductCategoryCreateView.as_view(), name='category_create'),
    path('categories/read/', category.categories, name='categories'),
    path('categories/update/<int:pk>/', category.ProductCategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', category.ProductCategoryDeleteView.as_view(), name='category_delete'),

    path('products/create/category/<int:pk>/', product.product_create, name='product_create'),
    path('products/read/category/<int:pk>/', product.products, name='products'),
    path('products/read/<int:pk>/', product.ProductDetailView.as_view(), name='product_read'),
    path('products/update/<int:pk>/', product.product_update, name='product_update'),
    path('products/delete/<int:pk>/', product.product_delete, name='product_delete'),
]