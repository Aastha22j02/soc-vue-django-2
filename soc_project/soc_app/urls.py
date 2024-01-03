from django.contrib import admin
from django.urls import path,include
from soc_app.views import TriggerViewSet
from rest_framework import routers
# from . import views


router = routers.DefaultRouter()
# router.register(r'users', UserAuthViewSet, basename="register")

router.register(r'trigger', TriggerViewSet, basename='trigger')

urlpatterns = [   
    path("", include(router.urls)),
    path('get_pipeline_status/', TriggerViewSet.as_view({'get': 'get_pipeline_status'}), name='get-pipeline-status'),

    
]