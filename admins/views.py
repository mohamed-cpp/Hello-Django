from django.contrib import admin
from django.http.response import Http404
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.db import connection
from django.contrib.auth.hashers import make_password
from django.contrib import messages


from admins.models import Phone
from .models import Admin
from .forms import AddAdmin, City, UslessForm
# Create your views here.

def index(request):
  admin_form = AddAdmin()
  admin_city = City(prefix='city', initial={'name': 'Cairo'})
  if request.method == "POST":
    admin_form = AddAdmin(request.POST, request.FILES)
    admin_city =  City(request.POST)
    #admin_form.errors
    if admin_form.is_valid() and admin_city.is_valid():
      admin = admin_form.save(commit=False)
      admin.password = make_password(request.POST['password'])
      admin.save()
      admin.city.add(admin_city.save())
      messages.success(request, 'Admin Added.')
      #return redirect('route-name', id=id)

  admins = Admin.objects.all()
  return render(request, 'admins/index.html', {
    'show' : True,
    'admins' : admins,
    'form' : admin_form,
    'form_city' : admin_city,
    'UslessForm' : UslessForm(),
  })



def calculate_db_response_time():
    sqltime = 0.0 # Variable to store execution time
    for query in connection.queries:
        sqltime += float(query["time"])  # Add the time that the query took to the total
    print("Page render: "+ str(sqltime)+ "sec for "+ str(len(connection.queries))+ " queries")

def show(request, name, id):
  admin = get_object_or_404(Admin, id=id) # best way in my opinion
  phones = Phone.objects.filter(admin_id=id)
  form = AddAdmin(request.POST or None, request.FILES or None, instance=admin )
  if request.method == "POST" and form.is_valid():
    admin = form.save(commit=False)
    admin.password = make_password(request.POST['password'])
    admin.save()
    messages.success(request, 'Admin Updated.')
  #print(admin.__dict__)
  #print(request.__dict__)
  calculate_db_response_time()
  return render(request, 'admins/show.html', {
      'admin' : admin,
      'phones' : phones,
      'form' : form,
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