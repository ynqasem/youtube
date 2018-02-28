from django import forms
from .models import Channel, Video
from django.contrib.auth.models import User

class ChannelForm(forms.ModelForm):
	class Meta:
		model = Channel
		fields = ["subscribers", "name", ]

class VideoForm(forms.ModelForm):
	class Meta:
		model = Video
		fields = ["name", "description", "video_link"]




