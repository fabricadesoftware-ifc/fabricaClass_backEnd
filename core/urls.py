from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from FabricaClass.views import TurmaViewSet, CursoViewSet, FormularioViewSet, RespostasViewSet, CriteriosViewSet, PerguntaViewSet
from usuario.router import router as usuario_router
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


router = DefaultRouter()
router.register(r"turmas", TurmaViewSet)
router.register(r"cursos", CursoViewSet)
router.register(r"formularios", FormularioViewSet)
router.register(r"respostas", RespostasViewSet)
router.register(r"criterios", CriteriosViewSet)
router.register(r"perguntas", PerguntaViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/", include(usuario_router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]