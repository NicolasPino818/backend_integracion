from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import *
from datetime import date
import requests


@api_view(['GET'])
def getData(request):
    data = Data.objects.last()
    serializer = DataSerializer(data)
    today = date.today().strftime("%Y-%m-%d")

    if request.method == 'GET':

        if serializer.data['fecha_actualizacion'] != today:
            r = getDolarRate(today)

            statusCode = r.status_code
            if statusCode == 200:
                jsonData = r.json()
                newData = {"usd_clp": jsonData['rates']
                           ['USD'], "fecha_actualizacion": today}
                newSerializer = DataSerializer(data=newData)

                if newSerializer.is_valid():
                    newSerializer.save()

                    responseObj = {
                        "success": True, "rate": newSerializer.data['usd_clp'], "date": newSerializer.data['fecha_actualizacion'], "database": False}

                    return JsonResponse(responseObj, status=status.HTTP_200_OK)

                else:
                    return JsonResponse({"success": False, "message": "Problema al serializar Json"}, status=status.HTTP_200_OK)

            else:
                return JsonResponse({"success": False, "message": "Api del dolar no disponible"}, status=status.HTTP_200_OK)
        else:
            responseObj = {"success": True, "rate": serializer.data['usd_clp'],
                           "date": serializer.data['fecha_actualizacion'], "database": True}
            return JsonResponse(responseObj, status=status.HTTP_200_OK)


def getDolarRate(date):
    header = {'apikey': 'kdN9eoYAtibCjxAky7HdhlA7xtFTZi78'}

    return requests.get(f"https://api.apilayer.com/fixer/{date}?symbols=USD&base=CLP", headers=header)


@api_view(['POST'])
def login_user(request):

    try:
        usuario = request.data['user']
        passw = request.data['passw']
    except:
        return JsonResponse({"success": False}, status=status.HTTP_400_BAD_REQUEST)

    cuenta = Usuarios.objects.filter(usuario=usuario).values()

    if cuenta.count() > 0:

        if request.method == 'POST':
            serializer = LoginSerializer(cuenta[0])

            if serializer.data['passw'] == passw:
                return JsonResponse({"success": True}, safe=False, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"success": False, "reason": "wrong password"}, safe=False, status=status.HTTP_200_OK)
    else:
        return JsonResponse({"success": False, "reason": "wrong email"}, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def getAllMarcas(request):
    marcas = Marcas.objects.all()
    serializer = MarcasSerializer(marcas)

    if request.method == 'GET':
        return JsonResponse({"success": True, "productos": serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def getAllCategorias(request):
    categorias = Categorias.objects.all()
    serializer = CategoriaSerializer(categorias)

    if request.method == 'GET':
        return JsonResponse({"success": True, "productos": serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def getAllProductos(request):
    productos = Productos.objects.all()
    serializer = ProductoSerializer(productos)

    if request.method == 'GET':
        return JsonResponse({"success": True, "productos": serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def getProductsByCategory(request, category):

    print(category)

    try:
        cat = Categorias.objects.filter(nom_categoria=category).values()
    except:
        return JsonResponse({"success": False}, status=status.HTTP_404_NOT_FOUND)

    if cat.count() > 0:
        productos = Productos.objects.filter(categoria=cat[0]['id'])

        serializer = ProductoSerializer(productos, many=True)

        print(productos)

        if productos.count() > 0:
            return JsonResponse({"success": True, "products": serializer.data}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({"success": True, "message": "no products in this category"}, status=status.HTTP_200_OK)

    else:
        return JsonResponse({"success": False}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def productById(request, id):

    try:
        producto = Productos.objects.get(pk=id)
    except producto.DoesNotExist:
        return JsonResponse({"success": False}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductoSerializer(producto)

    if request.method == 'GET':
        return JsonResponse({"success": True, "producto": serializer.data}, safe=False, status=status.HTTP_200_OK)
