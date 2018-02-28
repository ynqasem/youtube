from django.db import models
from django.contrib.auth.models import User

class Channel(models.Model):
	subscribers = models.PositiveIntegerField()
	name = models.CharField(max_length=200)
	creator = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Video(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField()
	channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
	video_link = models.URLField()


	def __str__(self):
		return self.name