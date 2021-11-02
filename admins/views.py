from django.shortcuts import render

# Create your views here.

def index(request):
  admins = [
    {"name": "mohamed"},
    {"name": "ahmed"},
  ]

  return render(request, 'admins/index.html', {
    'show' : True,
    'admins' : admins,
    'request' : request
  })


def show(request, name):
  admin = {"name": name }

  return render(request, 'admins/show.html', {
    'show' : True,
    'admin' : admin,
  })