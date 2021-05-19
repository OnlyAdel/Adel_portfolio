from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=250)
	description = models.TextField(max_length=500)
	date = models.DateField()
	def __str__(self):
		return self.title
