from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token  # Import Token authentication views

urlpatterns = [
    #admin urls
    path('admin/', admin.site.urls),
    path('api/', include('fcapi.urls')),
    path('', TemplateView.as_view(template_name='index.html')),
]


