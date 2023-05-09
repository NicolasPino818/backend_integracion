from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import *
from datetime import datetime, timezone, date
import requests
import json

api_view(['GET'])
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


api_view(['POST'])
@csrf_exempt
def login_user(request):

    print(request.body)

    try:
        usuario = request.data['user']
        passw = request.data['passw']
    except:
        return JsonResponse({"success":False}, status = status.HTTP_400_BAD_REQUEST)
    
    usuario = Usuarios.objects.filter(usuario = usuario)

    serializer = LoginSerializer(usuario)

    if request.method == 'POST':
        return JsonResponse({"success":True, "data":  serializer.data})