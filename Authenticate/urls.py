from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="auth-login"),
    path('register', views.register, name="auth-register"),
    path('logout', views.logoff, name="auth-logout"),
    path('webpage', views.dummypage, name="dummy-page")
]