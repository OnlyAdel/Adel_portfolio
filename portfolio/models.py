from django.db import models
 
class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=250, blank=True)
	image = models.ImageField(upload_to='portfolio/images/')
	url = models.URLField(blank=True)
	def __str__(self):
		return self.title

class Certificate(models.Model):
        title = models.CharField(max_length=100)
        description = models.TextField(max_length=250, blank=True)
        image = models.ImageField(upload_to='portfolio/images/')
        url = models.URLField(blank=True)
        slug = models.SlugField(null=True)
        def __str__(self):
                return self.title
                 
class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	subject = models.CharField(max_length=200)
	message = models.TextField()              
	
	def __str__(self):
		return self.subject 
