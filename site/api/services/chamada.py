from django.views.decorators.http import require_http_methods
from core.decorator import has_data_body, validate_dataclass
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpRequest
from chamada.models import Chamada, ChamadaAluno
from api.dto.chamada import chamada_create_dto
from oficinas.models import Oficinas
import json


@csrf_exempt
@require_http_methods(["POST"])
@validate_dataclass(chamada_create_dto.CreateChamada)
@has_data_body
def create_chamada(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    try:
        oficina = Oficinas.objects.get(id=data['oficina'])

    except Oficinas.DoesNotExist:
        return JsonResponse(
            {
                'success': False,
                'msg': 'Oficina does not exists'
            }, 
            status=422
        )

    chamada = Chamada(
        decricao=data['descricao'],
        oficina=oficina
    )

    chamada.save()

    return JsonResponse(
        {
            'success': True,
            'id': chamada.id,
        }, 
        status=201
    )
