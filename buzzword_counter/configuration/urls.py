"""buzzword_counter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import socket

from django.conf import settings
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from buzzword_counter.counter.views import CounterListView, IncreaseCounterView

urlpatterns = []
if settings.DEBUG:
    try:
        import pydevd_pycharm
    except:
        # we only have that package available on a custom build docker image
        # on "usual" deployments in the development cluster with docker images
        # that are also deployed in staging/production, we therefore can't use
        # the remote debugger
        pass

    def debug_settrace(request):
        # first three octets of docker container interface ip address
        ip_address = socket.gethostbyname(socket.gethostname()).rsplit(".", maxsplit=1)[
            0
        ]
        # substitute last octet for docker host interface
        ip_address = f"{ip_address}.1"
        port = 8200
        print(f"gonna settrace to {ip_address}:{port}")
        print(
            "Make sure to set correct path mappings of PyCharms python remote debugger!"
        )
        pydevd_pycharm.settrace(
            ip_address, port=port, stdoutToServer=True, stderrToServer=True
        )
        return HttpResponse("debugger started")

    urlpatterns += [
        path("debug_settrace/", debug_settrace),
    ]


urlpatterns += [
    path("admin/", admin.site.urls),
    path("increase-counter/", IncreaseCounterView.as_view(), name="increase-counter"),
    path("", CounterListView.as_view()),
]
