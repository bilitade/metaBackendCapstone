from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Menu
from .serializer import MenuSerializer

class MenuListView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer

    def get(self, request):
        items = Menu.objects.all()
        serializer = self.serializer_class(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        return Response({"status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class MenuDetailView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer

    def get(self, request, pk):
        try:
            item = Menu.objects.get(pk=pk)
        except Menu.DoesNotExist:
            return Response({"status": "error", "message": "Menu item not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(item)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            item = Menu.objects.get(pk=pk)
        except Menu.DoesNotExist:
            return Response({"status": "error", "message": "Menu item not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        return Response({"status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            item = Menu.objects.get(pk=pk)
        except Menu.DoesNotExist:
            return Response({"status": "error", "message": "Menu item not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        return Response({"status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            item = Menu.objects.get(pk=pk)
        except Menu.DoesNotExist:
            return Response({"status": "error", "message": "Menu item not found"}, status=status.HTTP_404_NOT_FOUND)

        item.delete()
        return Response({"status": "success", "message": "Menu item deleted"}, status=status.HTTP_204_NO_CONTENT)
