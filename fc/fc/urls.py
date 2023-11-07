from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  # Import Token authentication views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include the app's URLs
    path('', include('fcapi.urls')),
]


