from django.db import models


class Post(models.Model):
	name=models.CharField(max_length=200,blank=True,null=True)
	details=models.TextField(max_length=500,blank=True,null=True)
	link=models.URLField(max_length=200,blank=True,null=True)
	image=models.ImageField(default='placeholder.png',upload_to='thumbnails')
	github_repo = models.URLField(max_length=200,blank=True,null=True)

	def __str__(self):
		return self.name

