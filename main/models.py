from django.db import models
from django.contrib.auth.models import User

import json


class CSVFile(models.Model):
	name = models.CharField('Название', max_length=256, unique=True)
	file = models.FileField(upload_to='csvs')

	def __str__(self):
		return self.name
		
	class Meta:
		verbose_name = 'Файл'
		verbose_name_plural = 'Файлы'


class Task(models.Model):
	STATUSES = (
		(0, 'В очереди'),
		(1, 'В работе'),
		(2, 'Завершено')
	)
	user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
	csv = models.ForeignKey(CSVFile, on_delete=models.CASCADE, verbose_name='CSV Файл')
	status = models.IntegerField('Статус', choices=STATUSES, default=0)
	result = models.TextField('Результат', blank=True, null=True)

	def __str__(self):
		return f'{self.user.username} - {self.csv.name}'

	def set_result(self, result: list):
		self.result = json.dumps(result)
		self.save()
		
	def set_status(self, status: int):
		self.status = status
		self.save()

	@classmethod
	def get_task(cls, id: int):
		try:
			return cls.objects.get(id=id)
		except cls.DoesNotExist:
			return None

	class Meta:
		verbose_name = 'Задача'
		verbose_name_plural = 'Задачи'
