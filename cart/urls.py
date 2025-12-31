from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('session/add-product/', views.SessionAddProductView.as_view(), name='session-add-product'),
]