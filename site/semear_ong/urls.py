from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('api/', include('api.urls')),
    path('', include('core.urls')),
    path('oficinas/', include('oficinas.urls')),
    path('chamada/', include('chamada.urls')),
    path('orientador/', include('orientador.urls')),
    path('alunos/', include('alunos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
