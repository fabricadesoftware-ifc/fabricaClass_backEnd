from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from FabricaClass.views import TurmaViewSet, CursoViewSet

router = DefaultRouter()
router.register(r"turmas", TurmaViewSet)
router.register(r"cursos", CursoViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]