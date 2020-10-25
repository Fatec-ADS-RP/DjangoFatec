from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('', include('accounts.urls')),
    path('index/', include('website.urls')),
    path('topicos/', include('topicos.urls')),
]

