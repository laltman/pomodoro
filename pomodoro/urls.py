"""pomodoro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tasklist/$', 'todo.views.task_list'),
    url(r'^task/new/$', 'todo.views.task_new'),
    url(r'^task/(?P<pk>\d+)/edit', 'todo.views.task_edit'),
    url(r'^delete/(?P<pk>\d+)', 'todo.views.delete'),
    url(r'^task/(?P<pk>\d+)/pom', 'todo.views.pom'),
    url(r'^task/(?P<pk>\d+)/complete', 'todo.views.complete')
]
