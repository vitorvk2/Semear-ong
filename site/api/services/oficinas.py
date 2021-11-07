from api.dto.oficina import oficina_create_dto, oficina_aluno_create_dto, oficina_update_dto, oficina_delete_dto
from core.decorator import has_data_body, validate_dataclass, is_api_authenticated
from oficinas.models import Oficinas, OficinaAluno, OficinaImagem
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.views.decorators.http import require_http_methods
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpRequest
from orientador.models import Orientador
from alunos.models import Alunos
from django.conf import settings
from core.models import User
from io import BytesIO
from PIL import Image
import json
import sys


@csrf_exempt
@require_http_methods(["POST"])
@validate_dataclass(oficina_create_dto.CreateOficina)
@has_data_body
@is_api_authenticated
def create_oficina(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    try:
        orientador = Orientador.objects.get(id=data['orientador'])

    except Orientador.DoesNotExist:
        return JsonResponse(
            {
                'success': False,
                'msg': 'Orientador does not exists'
            }, 
            status=422
        )

    oficina = Oficinas(
        nome=data['nome'],
        descricao=data['descricao'],
        local=data['local'],
        link=data['link'],
        horario=data['horario_aula'],
        orientador=orientador,
    )

    oficina.save()

    return JsonResponse(
        {
            'success': True,
            'id': oficina.id,
        }, 
        status=201
    )


@csrf_exempt
@require_http_methods(["GET"])
@is_api_authenticated
def get_oficina_by_id(request: HttpRequest, id: str) -> JsonResponse:
    if request.is_admin:
        oficina = Oficinas.objects.filter(id=id, deleted=0)
    
    else:
        oficina = Oficinas.objects.filter(id=id, deleted=0, orientador_id=request.id_user)

    oficina = oficina.values(
        "nome",
        "id",
        "descricao",
        "local",
        "link",
        "horario",
        "orientador__id",
        "orientador__user__nome",
        "created_at",
        "is_active"
    )

    if not oficina.exists():
        return JsonResponse(
            {
                'success': False,
                'msg': 'Id not found'
            }, 
            status= 422
        )

    imagens = OficinaImagem.objects.filter(oficina_id__in=list(oficina.values_list('id', flat=True))).values('oficina', 'img')
    imagens_dict = {}

    for i in imagens:
        if i['oficina'] not in imagens_dict:
            imagens_dict[i['oficina']] = []
        imagens_dict[i['oficina']].append(i['img'])

    oficina = list(oficina)

    for index, i in enumerate(oficina):
        oficina[index]['imagens'] = imagens_dict.get(i['id'], [])

    return JsonResponse(
        {
            'success': True,
            'oficina': oficina[0],
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["GET"])
@is_api_authenticated
def get_oficina(request: HttpRequest) -> JsonResponse:
    if request.is_admin:
        oficina = Oficinas.objects.filter(deleted=0)

    else:
        oficina = Oficinas.objects.filter(deleted=0, orientador_id=request.id_user)

    oficina = oficina.order_by("-id").values(
        "nome",
        "id",
        "descricao",
        "local",
        "link",
        "horario",
        "orientador__id",
        "orientador__user__nome",
        "created_at",
        "is_active"
    )[:30]

    imagens = OficinaImagem.objects.filter(oficina_id__in=list(oficina.values_list('id', flat=True))).values('oficina', 'img')
    imagens_dict = {}

    for i in imagens:
        if i['oficina'] not in imagens_dict:
            imagens_dict[i['oficina']] = []
        imagens_dict[i['oficina']].append(i['img'])

    oficina = list(oficina)

    for index, i in enumerate(oficina):
        oficina[index]['imagens'] = imagens_dict.get(i['id'], [])

    return JsonResponse(
        {
            'success': True,
            'oficina': oficina,
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["PUT"])
@validate_dataclass(oficina_update_dto.UpdateOficina)
@has_data_body
@is_api_authenticated
def update_oficina(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    if request.is_admin:
        oficina = Oficinas.objects.filter(id=data['id'], deleted=0)

    else:
        oficina = Oficinas.objects.filter(id=data['id'], deleted=0, orientador_id=request.id_user)

    if not oficina.exists():
        return JsonResponse(
        {
            'success': False,
            'msg': 'Oficina does not exists'
        }, 
        status=200
    )
    
    oficina.update(
        nome=data['nome'], 
        descricao=data['descricao'] , 
        horario=data['horario_aula'] , 
        local=data['local'], 
        link=data['link']
    )

    return JsonResponse(
        {
            'success': True,
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["DELETE"])
@validate_dataclass(oficina_delete_dto.DeleteOficina)
@has_data_body
@is_api_authenticated
def delete_oficina(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    if request.is_admin:
        oficina = Oficinas.objects.filter(id=data['id'], deleted=0)

    else:
        oficina = Oficinas.objects.filter(id=data['id'], deleted=0, orientador_id=request.id_user)

    if not oficina.exists():
        return JsonResponse(
        {
            'success': False,
            'msg': 'Oficina does not exists'
        }, 
        status=200
    )
    
    oficina.update(deleted=1)

    return JsonResponse(
        {
            'success': True,
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["POST"])
@validate_dataclass(oficina_aluno_create_dto.CreateOficinaAluno)
@has_data_body
@is_api_authenticated
def create_aluno_oficina(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    try:
        if request.is_admin:
            oficina = Oficinas.objects.get(id=data['oficina_id'])

        else:
            oficina = Oficinas.objects.get(id=data['oficina_id'], orientador_id=request.id_user)

        aluno = Alunos.objects.get(id=data['aluno_id'])

    except (Alunos.DoesNotExist, Oficinas.DoesNotExist):
        return JsonResponse(
            {
                'success': False,
                'msg': 'Oficina and/or Aluno does not exists'
            }, 
            status=422
        )

    oficina = OficinaAluno(
        oficina=oficina,
        aluno=aluno      
    )

    oficina.save()

    return JsonResponse(
        {
            'success': True,
            'id': oficina.id,
        }, 
        status=201
    )


@csrf_exempt
@require_http_methods(["GET"])
def get_oficina_aluno_by_id(request: HttpRequest, id: str) -> JsonResponse:
    if request.is_admin:
        oficina = OficinaAluno.objects.filter(id=id, deleted=0).values()

    else:
        oficina = OficinaAluno.objects.filter(id=id, deleted=0, orientador_id=request.id_user).values()

    if not oficina.exists():
        return JsonResponse(
            {
                'success': False,
                'msg': 'Id not found'
            }, 
            status= 422
        )

    return JsonResponse(
        {
            'success': True,
            'oficina_aluno': oficina[0],
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["GET"])
@is_api_authenticated
def get_oficina_aluno(request: HttpRequest, id_oficina: str) -> JsonResponse:
    if request.is_admin:
        oficina = OficinaAluno.objects.filter(deleted=0, oficina_id=id_oficina)

    else:
        oficina = OficinaAluno.objects.filter(deleted=0, oficina_id=id_oficina, oficina__orientador_id=request.id_user)

    oficina = oficina.order_by("-id").values(
        "id",
        "oficina__nome",
        "aluno__user__nome",
        "aluno_id",
        "created_at"
    )[:30]

    return JsonResponse(
        {
            'success': True,
            'oficina_alunos': list(oficina),
        }, 
        status=200
    )

@csrf_exempt
@require_http_methods(["GET"])
def get_five_oficina(request: HttpRequest) -> JsonResponse:
    oficina = Oficinas.objects.filter(deleted=0).order_by("-id").values(
        "nome",
        "id",
        "descricao",
        "orientador__user__nome",
        "created_at",
        "is_active"
    )[:5]

    imagens = OficinaImagem.objects.filter(oficina_id__in=list(oficina.values_list('id', flat=True))).values('oficina', 'img')
    imagens_dict = {}

    for i in imagens:
        if i['oficina'] not in imagens_dict:
            imagens_dict[i['oficina']] = []
        imagens_dict[i['oficina']].append(i['img'])

    oficina = list(oficina)

    for index, i in enumerate(oficina):
        oficina[index]['imagens'] = imagens_dict.get(i['id'], [])

    return JsonResponse(
        {
            'success': True,
            'oficina': oficina,
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["POST"])
@validate_dataclass(oficina_delete_dto.DeleteOficina)
@has_data_body
@is_api_authenticated
def get_aluno_oficinas_inscrito(request: HttpRequest) -> JsonResponse:
    data = json.loads(request.body) 

    oficina = Oficinas.objects.filter(oficinaaluno__aluno_id=data['id'], deleted=0).order_by("-id").values(
        "nome",
        "id",
        "descricao",
        "orientador__user__nome",
        "created_at",
        "horario",
        "is_active"
    )

    imagens = OficinaImagem.objects.filter(oficina_id__in=list(oficina.values_list('id', flat=True))).values('oficina', 'img')
    imagens_dict = {}

    for i in imagens:
        if i['oficina'] not in imagens_dict:
            imagens_dict[i['oficina']] = []
        imagens_dict[i['oficina']].append(i['img'])

    oficina = list(oficina)

    for index, i in enumerate(oficina):
        oficina[index]['imagens'] = imagens_dict.get(i['id'], [])

    return JsonResponse(
        {
            'success': True,
            'oficinas': oficina,
        }, 
        status=200
    )


@csrf_exempt
@require_http_methods(["POST"])
def add_image_oficina(request: HttpRequest) -> JsonResponse:
    try:
        oficina = Oficinas.objects.get(id=request.POST.get('id'))
    
    except Oficinas.DoesNotExist:
        return JsonResponse(
            {
                'success': False,
                'msg': 'Id not found'
            }, 
            status= 422
        )

    image = Image.open(request.FILES['img'])
    width, height = image.size
    o = BytesIO()

    if width > 1024:
        height = (1024 * height) / width
        image = image.resize((1024, int(height)), Image.ANTIALIAS)

    image.save(o, format='WEBP', quality=100)
    o.seek(0)

    name = User.objects.make_random_password(20)

    file = InMemoryUploadedFile(o, 'ImageField', "%s.webp" % name, 'image/webp', sys.getsizeof(o), None)
    fs = FileSystemStorage(location=settings.MEDIA_ROOT + f"/oficinas/")

    fs.save((name + "." + file.name.split('.')[-1]).lower(), file)
    nameimg = f"/media/oficinas/{name}.webp".lower()

    OficinaImagem(oficina=oficina, img=nameimg).save()

    return JsonResponse(
        {
            'success': True,
            'path': nameimg
        }, 
        status=200
    )