from django.db import models


class Departamentos(models.Model):
	nombre = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre