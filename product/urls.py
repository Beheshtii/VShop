from django.urls import path, re_path
from . import views

app_name = 'product'

urlpatterns = [
    path('grid/', views.ProductGridView.as_view(), name='product-grid'),
    path('list/', views.ProductListView.as_view(), name='product-list'),
    path(r'detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
]