# project/urls.py
from django.contrib import admin
from django.urls import path, include  # Import the include function

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include('userAuth_app.urls')),
    path('api/v2/', include('soc_app.urls')),
    path("api/v3/", include('rule__api.urls')),  # Include your app's URLs here
]
