"""View for teacher."""
from django.views import View
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from core.managers.teacher_manager import TeacherManager
from core.models.teacher import Teacher
from core.serializers.serializers import TeacherSerializer
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from rest_framework import permissions
from core.permissions.acl_manager import IsTeacherUser


@method_decorator(csrf_exempt, name='dispatch')
class TeacherListView(APIView):

    permission_classes = [permissions.IsAuthenticated, IsTeacherUser]

    def __init__(self, **kwargs) -> None:
        self.tr_mgr = TeacherManager()
        super().__init__(**kwargs)
        

    def get(self, request):
        permission_classes = [permissions.IsAuthenticated, IsTeacherUser]
        teacher_objs = self.tr_mgr.load_all()

        teacher_data = TeacherSerializer(teacher_objs, many=True).data

        if not teacher_data:
            return JsonResponse(status=status.HTTP_400_BAD_REQUEST)
        response_data = teacher_data
        return JsonResponse(response_data, safe=False)

    def post(self, request, format=None):
        data = request.data
        if type(data) == list:
            serializer = TeacherSerializer(data=data, many=True)
        else:
            serializer = TeacherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response_data = serializer.data
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
class TeacherDetailView(APIView):
    def get(self, request, pk):
        teacher = Teacher.objects.filter(pk=pk).first()
        if not teacher:
            return JsonResponse({"result": "Teacher is not available at this id"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TeacherSerializer(teacher)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        teacher = Teacher.objects.filter(pk=pk).first()
        if not teacher:
            return Response(status=status.HTTP_404_NOT_FOUND)

        data = request.data
        if type(data) == list:
            serializer = TeacherSerializer(data=data, many=True)
        else:
            serializer = TeacherSerializer(data=data)
        if serializer.is_valid():
            serializer.save(partial=True)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        teacher = Teacher.objects.filter(pk=pk).first()
        if not teacher:
            return Response(status=status.HTTP_404_NOT_FOUND)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)