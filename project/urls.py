from django.contrib import admin
from django.urls import path, include  # ⬅️ importante

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),  # ⬅️ agora está apontando pro app
]
