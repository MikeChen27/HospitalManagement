"""Hospital URL Configuration

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
from django.contrib import admin
from django.urls import path
from Hos import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login),
    path('search/patient/', views.search_pat),
    path('search/caregiver/', views.search_cg),
    path('search/admission/', views.search_adm),
    path('search/cpt/', views.search_cpt),
    path('search/datatimeevent/', views.search_dt),
    path('search/labevent/', views.search_lab),
    path('search/prescription/', views.search_pre),
    path('add/patient/', views.add_pat),
    path('add/caregiver/', views.add_cg),
    path('add/admission/', views.add_adm),
    path('add/cpt/', views.add_cpt),
    path('add/datatimeevent/', views.add_dt),
    path('add/labevent/', views.add_lab),
    path('add/prescription/', views.add_pre),
    path('edit/patient/', views.edit_pat),
    path('edit/caregiver/', views.edit_cg),
    path('edit/admission/', views.edit_adm),
    path('edit/cpt/', views.edit_cpt),
    path('edit/datatimeevent/', views.edit_dt),
    path('edit/labevent/', views.edit_lab),
    path('edit/prescription/', views.edit_pre),
    path('delete/admission/', views.del_adm),
    path('delete/cpt/', views.del_cpt),
    path('delete/datatimeevent/', views.del_dt),
    path('delete/labevent/', views.del_lab),
    path('delete/patient/', views.del_pat),
    path('delete/prescription/', views.del_pre),
    path('delete/caregiver/', views.del_cg),
    path('home/', views.home),
]
