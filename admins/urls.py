from django.urls import path
from . import views

urlpatterns = [
    path('admin', views.index),
    path('admin/show/<slug:name>', views.show, name="adminroute")
]
