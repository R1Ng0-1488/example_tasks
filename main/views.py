from rest_framework import viewsets, mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Task
from .serializers import CreateTaskSerializer, TaskListSerializer


class TaskViewSet(viewsets.GenericViewSet):
	"""Создание и отображение задач"""
	queryset = Task.objects.all()
	serializer_class = TaskListSerializer
	permission_classes = [IsAuthenticated]


class TaskRetrieveListViewSet(TaskViewSet):
	
	def list(self, request):
		"""показывает количество задач на вычисление, которые на текущий момент в работе"""
		queryset = self.queryset.filter(status=1)
		serializer = TaskListSerializer(queryset, many=True)
		return Response(serializer.data)
	
	def retrieve(self, request, pk=None):
		"""принимает ID задачи и отображает результат в JSON-формате"""
		task = get_object_or_404(self.queryset, pk=pk)
		serializer = TaskListSerializer(task)
		return Response(serializer.data)


class TaskCreateViewSet(mixins.CreateModelMixin, TaskViewSet):
	serializer_class = CreateTaskSerializer

	def create(self, request):
		"""получает по HTTP имя CSV-файла (пример файла во вложении) в хранилище и суммирует каждый 10й столбец
		"""
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save(request.user)
			return Response({'name': serializer.csv.name}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
