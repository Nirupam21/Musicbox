"""mymusic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from music import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',views.welcome),
    path('home/',views.home),
    path('auth/',views.auth_view),
    path('uploads/',views.uploadpage),
    path('logout/',views.logout),
    path('upload/',views.upload),
    path('myuploads/',views.myUploads),
    #re_path(r'myuploads/(\d+)/',views.uploadplay),
    re_path(r'play/(\d+)/',views.play),
    path('welcome/',views.welcome),
    path('login/',views.login),
    path('signup/',views.UserFormView.as_view()),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]