# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view,  permission_classes

# # NOTE: Ejemplo de hello world con método GET
# @api_view(['GET'])
# def hello_world(request):
#     template = '<h1>Hello world Django APIs!</h1>' 
#     return HttpResponse(template)




@api_view(['GET', 'POST'])
@permission_classes([]) 
def inicio(request):

    template = f'<h1>{request.GET.get("pagina_principal")}</h1>'
    
    print(template)
    return HttpResponse(template)


@api_view(['GET', 'POST'])
@permission_classes([]) 
def compras(request):

    template = f'<h1>{request.GET.get("pagina_de_compras")}</h1>'

    print(template)
    return HttpResponse(template)


@api_view(['GET', 'POST'])
@permission_classes([]) 
def productos(request):
    
    template = f'<h1>{request.GET.get("productos_venta")}</h1>'
    
    print(template)
    return HttpResponse(template)
