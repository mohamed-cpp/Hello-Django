from django.contrib import admin
from django.http.response import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Admin
# Create your views here.

def index(request):
  admins = Admin.objects.all()
  return render(request, 'admins/index.html', {
    'show' : True,
    'admins' : admins
  })


def show(request, name, id):
  admin = get_object_or_404(Admin, id=id) # best way in my opinion
  return render(request, 'admins/show.html', {
      'admin' : admin,
    })
  ''' Another way to retuen 404
  try:
    admin = Admin.objects.get(id=id)
    return render(request, 'admins/show.html', {
      'admin' : admin,
    })
  except Exception as e:
    #return render(request, 'errors/404.html')
    raise Http404
  '''