from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('main/', views.index_view, name='main'),
    path('',views.SigupPage,name="signup"),
    path('login/', views.LoginPage, name='login'),
    path('logout/',views.LogoutPage, name='logout'),
    path('shop/',views.shop,name='shop'),
    path('add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('show_cart/', views.show_cart, name='show_cart'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)