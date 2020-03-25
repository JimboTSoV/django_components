"""sandbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from sandbox import settings
from sandbox.pages.views import PageView

urlpatterns = [
  path('admin/', admin.site.urls),
  path('pages/', include('sandbox.pages.urls')),
  path("home/", PageView.as_view(), {'slug': 'home'}, name="home"),
  path("home/<slug:slug>", PageView.as_view(), name="page_via_path"),
  path("home/<path:path>/<slug:slug>", PageView.as_view(), name="page_via_path"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
