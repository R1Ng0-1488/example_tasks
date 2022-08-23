from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task, CSVFile
from .tasks import start_task


class CreateTaskSerializer(serializers.ModelSerializer):
	name = serializers.CharField(max_length=256)

	class Meta:
		model = Task
		fields = ('name',)

	def validate_name(self, data):
		try:
			self.csv = CSVFile.objects.get(name=data)
		except CSVFile.DoesNotExist:
			raise serializers.ValidationError(f'There is not csv with this {data} name')

	def create(self, *args, **kwargs):
		task = Task.objects.create(user=kwargs.get('user'), csv=self.csv)
		start_task.delay(task.id)
		return task

	def save(self, user):
		return self.create(user=user)


class CSVFileSerializer(serializers.ModelSerializer):
	class Meta:
		model = CSVFile
		fields = '__all__'


class TaskListSerializer(serializers.ModelSerializer):
	csv = CSVFileSerializer()
	user = serializers.SerializerMethodField()
	status = serializers.SerializerMethodField()

	class Meta:
		model = Task
		fields = '__all__'

	def get_user(self, obj):
		return obj.user.username

	def get_status(self, obj):
		return obj.get_status_display()
