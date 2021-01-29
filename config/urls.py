"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include, path, re_path
from django.conf.urls import handler404
from .views import error400, error403, error404, error500

handler400 = error400
handler403 = error403
handler404 = error404
handler500 = error500

urlpatterns = [
    path('', include('apps.account.urls')),
    path('admin/', admin.site.urls),
    path('advance/', include('apps.advance.urls')),
    path('client/', include('apps.client.urls')),
    path('company/', include('apps.company.urls')),
    path('project/', include('apps.project.urls')),
    path('reimburse/', include('apps.reimburse.urls')),
    path('timesheet/', include('apps.timesheet.urls')),
]
