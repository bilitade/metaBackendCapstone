from django.shortcuts import render
from django.http import HttpResponse;
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, Menu
from .serializer import MenuSerializer, BookingSerializer
class MenuView(APIView):
    
    def get(self, request):
        item=Menu.objects.all()
        serializer=MenuSerializer(item, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer=MenuSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response({"status": "success", "data":serializer.data})
        
        
    
    