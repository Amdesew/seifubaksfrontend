from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Fuel, oil
from rest_framework.response import Response
from .serializers import FuelSerializer, OilSerializer
from django.middleware.csrf import get_token


class FuelViewSet(viewsets.ModelViewSet):
    queryset = Fuel.objects.all()
    serializer_class = FuelSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)  # Log the incoming data
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def csrf_token(request):
        token = get_token(request)
        return JsonResponse({'csrfToken': token})


class OilViewSet(viewsets.ModelViewSet):
    queryset = oil.objects.all()
    serializer_class = OilSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)  # Log the incoming data
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def csrf_token(request):
        token = get_token(request)
        return JsonResponse({'csrfToken': token})

def Home(request):
    return render(request, 'home.html')

def car_fuel(request):
    car_fuel = Fuel.objects.all()
    return render(request, 'fuel_table.html', {'fuel': car_fuel})

def car_oil(request):
    car_oil = oil.objects.all()
    return render(request, 'oil_table.html', {'oil': car_oil})