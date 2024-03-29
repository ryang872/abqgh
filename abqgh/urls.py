"""abqgh URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from upload.views import HomePageView

urlpatterns = [
    path('abqgh/admin/', admin.site.urls),
    path('abqgh/', HomePageView.as_view(), name='home'),
    path('abqgh/tiplist/', include('upload.urls')),
    path('abqgh/comments/', include('django_comments.urls')),
    path('abqgh/gatecode/', include('gatecode.urls')),
    path('abqgh/maps/', include('maps.urls')),
    # path('', include('pwa.urls')),
    path('abqgh/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('abqgh/logout/', LogoutView.as_view(template_name='logged_out.html'), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

