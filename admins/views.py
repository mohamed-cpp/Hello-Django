from django.contrib import admin
from django.http.response import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db import connection

from admins.models import Phone
from .models import Admin
# Create your views here.

def index(request):
  admins = Admin.objects.all()
  return render(request, 'admins/index.html', {
    'show' : True,
    'admins' : admins
  })

def calculate_db_response_time():
    sqltime = 0.0 # Variable to store execution time
    for query in connection.queries:
        sqltime += float(query["time"])  # Add the time that the query took to the total
    print("Page render: "+ str(sqltime)+ "sec for "+ str(len(connection.queries))+ " queries")

def show(request, name, id):
  admin = get_object_or_404(Admin, id=id) # best way in my opinion
  phones = Phone.objects.filter(admin_id=id)
  #print(admin.__dict__)
  #print(request.__dict__)
  calculate_db_response_time()
  return render(request, 'admins/show.html', {
      'admin' : admin,
      'phones' : phones,
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