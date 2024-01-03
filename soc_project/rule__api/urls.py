# urls.py
from django.urls import path
from .views import RuleListByCategory, RuleList, OnboardViewSet
from django.contrib import admin
from django.urls import path,include

from rest_framework import routers
# from . import views


router = routers.DefaultRouter()
# router.register(r'users', UserAuthViewSet, basename="register")

router.register(r'onboard', OnboardViewSet, basename='onboard')

urlpatterns = [
    # ... your other patterns
    path("", include(router.urls)),
    path('rules/', RuleList.as_view(), name='rule-list'),
    path('rules/category/<str:category_name>/', RuleListByCategory.as_view(), name='rule-list-by-category'),
]
