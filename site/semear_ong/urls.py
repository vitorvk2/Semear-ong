from django.urls import path, include

urlpatterns = [
    path('api/', include('api.urls')),
    path('', include('core.urls')),
    path('oficinas/', include('oficinas.urls')),
    path('chamada/', include('chamada.urls')),
    path('alunos/', include('alunos.urls')),
]