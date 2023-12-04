"""
URL configuration for speechwell project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from resources.views import TherapistListView, TherapistByLocationListView
from disorders.views import DisorderListView, DisorderDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('allauth.urls')),
    path('resources/', include('resources.urls')),
    path('therapists/', TherapistListView.as_view(), name='therapist_list'),
    path('therapists/<str:location>/', TherapistByLocationListView.as_view(), name='therapists_by_location'),
    path('disorders/', DisorderListView.as_view(), name='disorder_list'),
    path('disorders/<slug:slug>/', DisorderDetailView.as_view(), name='disorder_detail'),

]