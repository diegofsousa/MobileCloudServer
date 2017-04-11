"""CloudServerAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from .views import StatusView, OrderView, MaxView, MinView, SumView

helper_patterns = [
	url(r'^$', StatusView.as_view(), name='status'),
    url(r'^order/$', OrderView.as_view(), name='order'),
    url(r'^sum/$', SumView.as_view(), name='sum'),
    url(r'^max/$', MaxView.as_view(), name='max'),
    url(r'^min/$', MinView.as_view(), name='min'),
    #url(r'^sum', include('api.urls')),
]

urlpatterns = helper_patterns
