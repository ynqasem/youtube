from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from youtubeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("list/", views.list, name="list"),
    path("detail/<int:channel_id>/", views.detail, name="detail"),
    path("create/", views.create, name="create"),
    path("update/<int:channel_id>/", views.update, name="update"),
    path("delete/<int:channel_id>/", views.delete, name="delete"),
    path("video/create/<int:channel_id>/", views.create_video, name="createv"),

]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)