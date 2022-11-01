from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('administrator/', include('administrator.urls')),
    path('admin/', admin.site.urls),
]
