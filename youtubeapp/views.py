from django.shortcuts import render, redirect

from .models import Channel, Video 
from .forms import ChannelForm, VideoForm

def list(request):
	obj = Channel.objects.all()
	context = {
		"obj": obj
	}
	return render(request, "list.html", context)

def detail(request, channel_id):
	obj = Channel.objects.get(id=channel_id)
	context = {
		"obj":obj
	}
	return render(request, "detail.html", context)

def create(request):
	form = ChannelForm()
	if request.method == "POST":
		form = ChannelForm(request.POST)
		if form.is_valid():
			channel = form.save(commit=False)
			channel.creator = request.user 
			channel.save()
			return redirect("list")
	context = {
	"form": form
	}
	return render(request, 'create.html', context)


def update(request, channel_id):
	channel_obj = Channel.objects.get(id=channel_id)
	form = ChannelForm(instance = channel_obj)
	if request.method == "POST":
		form = ChannelForm(request.POST, instance=channel_obj)
		if form.is_valid():
			form.save()
			return redirect("detail", channel_id=channel_obj.id)
	context = {
	"form": form,
	"channel_obj": channel_obj
	}
	return render(request, 'update.html', context)


def delete(request, channel_id):
	Channel.objects.get(id=channel_id).delete()
	return redirect('list')


def create_video(request, channel_id):
	channel_obj = Channel.objects.get(id=channel_id)
	form = VideoForm()
	if request.method == "POST":
		form = VideoForm(request.POST)
		if form.is_valid():
			video = form.save(commit = False)
			video.channel = channel_obj
			video.save()
			return redirect("detail", channel_id=channel_obj.id)
	context = {
	"form":form,
	"channel_obj": channel_obj,
	}

	return render(request, 'create_video.html', context)	