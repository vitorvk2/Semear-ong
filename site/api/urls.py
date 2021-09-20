from api.services import chamada
from django.urls import path

urlpatterns = [
    #! Chamada

    path('chamada/create/', chamada.create_chamada),
]