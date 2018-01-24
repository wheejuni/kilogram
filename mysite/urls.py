"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from kilogram import views as kilogram_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', login_required(kilogram_views.IndexView.as_view()), name='root'),
    url(r'^kilogram/', include('kilogram.urls')),

    #Account-related views.
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/signup$', kilogram_views.CreateUserView.as_view(), name='signup'),
    url(r'^accounts/signup/done$', kilogram_views.RegistrationCompletedView.as_view(), name='created_user'),

    url('', include('social_django.urls', namespace='social')),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
