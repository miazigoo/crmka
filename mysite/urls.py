from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('order.urls')),
    path('', include('Tasks.urls')),
    path('', include('customer.urls')),
]