from django.contrib import admin
from django.urls import path,include
from userAuth_app.views import UserAuthViewSet, LoginViewSet
from rest_framework import routers
# from . import views


router = routers.DefaultRouter()
# router.register(r'users', UserAuthViewSet, basename="register")

router.register(r'login', LoginViewSet, basename='login')

urlpatterns = [
    
    path("", include(router.urls))
    
]