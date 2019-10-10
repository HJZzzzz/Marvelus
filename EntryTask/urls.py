"""EntryTask URL Configuration

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
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from EventCenter.views_helper import index, event_detail_a

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('EventCenter.urls')),
    path('new/', include('luminus.urls')),

    # path('event-center/index/', index, name='event_index'),
    # path('event-center/event/<int:event_id>/', event_detail_a, name='detail'),

    path('index/', TemplateView.as_view(template_name="index.html"), name='frontend'),
    path('', TemplateView.as_view(template_name="index.html"), name='frontend'),
]
