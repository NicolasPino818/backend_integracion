from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *
from .serializers import *