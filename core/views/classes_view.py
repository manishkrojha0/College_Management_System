


from django.views import View
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from core.managers.classes_manager import ClassesManager
from core.models.classes import Classes
from core.serializers.serializers import ClassSerializer



@method_decorator(csrf_exempt, name='dispatch')
class ClassListView(APIView):
    def get(self, request):
        classes = Classes.objects.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        if type(data) == list:
            serializer = ClassSerializer(data=data, many=True)
        else:
            serializer = ClassSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class ClassDetailView(APIView):
    def get(self, request, pk):
        cls = Classes.objects.filter(pk=pk).first()
        if not cls:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ClassSerializer(cls)
        return Response(serializer.data)

    def put(self, request, pk):
        cls = Classes.objects.filter(pk=pk).first()
        if not cls:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ClassSerializer(cls, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cls = Classes.objects.filter(pk=pk).first()
        if not cls:
            return Response(status=status.HTTP_404_NOT_FOUND)
        cls.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
