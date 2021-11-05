from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.index, name="admins"),
    path('admin/show/<slug:name>/<id>/', views.show, name="adminroute")
]
