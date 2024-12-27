from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Menu
from .serializer import MenuSerializer
from rest_framework.permissions import IsAuthenticated

class MenuView(APIView):
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
        return Response({"status": "error", "errors": serializer.errors}, status=400)

