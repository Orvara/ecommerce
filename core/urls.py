from django.urls import path
from .views import (
    ItemDetailView,
    HomeView,
    checkout,
    add_to_cart,
    remove_from_cart
    )

app_name = 'core'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('checkout/',checkout,name='checout'),
    path('product/<slug>/',ItemDetailView.as_view(),name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove_from_cart'),

]
