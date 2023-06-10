from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('main/', views.index_view, name='main'),
    path('',views.SigupPage,name="signup"),
    path('login/', views.LoginPage, name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)