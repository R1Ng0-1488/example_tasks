from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Task
from .serializers import CreateTaskSerializer, TaskListSerializer


class TaskViewSet(viewsets.ViewSet):
	"""Создание и отображение задач"""
	queryset = Task.objects.all()
	serializer_class = CreateTaskSerializer
	permission_classes = [IsAuthenticated]

	def list(self, request):
		"""показывает количество задач на вычисление, которые на текущий момент в работе"""
		queryset = self.queryset.filter(status=1)
		serializer = TaskListSerializer(queryset, many=True)
		return Response(serializer.data)

	def create(self, request):
		"""получает по HTTP имя CSV-файла (пример файла во вложении) в хранилище и суммирует каждый 10й столбец"""
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			serializer.save(request.user)
			return Response({'result': 'succesfully created'}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def retrieve(self, request, pk=None):
		"""принимает ID задачи из п.1 и отображает результат в JSON-формате"""
		task = get_object_or_404(self.queryset, pk=pk)
		serializer = TaskListSerializer(task)
		return Response(serializer.data)
