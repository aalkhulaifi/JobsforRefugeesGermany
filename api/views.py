from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from .serializers import UserCreateSerializer,UserLoginSerializer, TaskerCreateSerializer,TaskerLoginSerializer, Task_RequestCreateSerializer
# User create and signin view
class UserCreateAPIView(CreateAPIView):
	serializer_class = UserCreateSerializer

	
class UserLoginAPIView(APIView):
	serializer_class = UserLoginSerializer

	def post(self, request):
		my_data = request.data
		serializer = UserLoginSerializer(data=my_data)
		if serializer.is_valid(raise_exception=True):
			valid_data = serializer.data
			return Response(valid_data, status=HTTP_200_OK)
		return Response(serializer.errors, HTTP_400_BAD_REQUEST)

# Tasker create and signin view

class TaskerCreateAPIView(CreateAPIView):
	serializer_class = TaskerCreateSerializer

	
class TaskerLoginAPIView(APIView):
	serializer_class = TaskerLoginSerializer

	def post(self, request):
		my_data = request.data
		serializer = TaskerLoginSerializer(data=my_data)
		if serializer.is_valid(raise_exception=True):
			valid_data = serializer.data
			return Response(valid_data, status=HTTP_200_OK)
		return Response(serializer.errors, HTTP_400_BAD_REQUEST)

# create task request
class Task_RequestAPIView(CreateAPIView):
	serializer_class = Task_RequestCreateSerializer

