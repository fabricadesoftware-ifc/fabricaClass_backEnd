from django.contrib import admin
from django.urls import include,path
from usuario.router import router as usuario_router
from FabricaClass.views import SendEmailView
import requests

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(usuario_router.urls)),
    path('send-email/', SendEmailView.as_view(), name='email'),
]
