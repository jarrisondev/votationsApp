from .models import User, Rol
from django.shortcuts import render, redirect
from django.http import HttpRequest

def dash(request: HttpRequest):
  return render(request, 'index.html')

# users
def users(request):
  users = User.objects.all().values()

  for user in users:
    rol_name = Rol.objects.get(id= user['rol_id'])
    user['rol'] = rol_name.name
  
  context = {
    'users' : users
  }
  return render(request, 'user/users.html', context)

def createUser(request: HttpRequest):
  
  if(request.method == 'POST'):
    name = request.POST.get('name')
    lastName = request.POST.get('lastName')
    password = request.POST.get('password')
    dni = request.POST.get('dni')
    idRol = request.POST.get('idRol')
    rol = Rol.objects.get(id=idRol)

    user = User(name=name, lastName=lastName, password =password, dni=dni, rol=rol)
    user.save()
    return redirect('/administrator/users/')


  roles = Rol.objects.all().values()

  context = {
    'roles': roles
  }

  return render(request, 'user/createUser.html', context)

def updateUser(request: HttpRequest, id):
  
  user = User.objects.get(id=id)

  if(request.method == 'POST'):
    name = request.POST.get('name')
    lastName = request.POST.get('lastName')
    idRol = request.POST.get('idRol')
    rol = Rol.objects.get(id=idRol)

    user.name = name
    user.lastName = lastName
    user.rol = rol
    user.save()

    return redirect('/administrator/users/')

  roles = Rol.objects.all().values()

  context = {
    'user': user,
    'roles': roles
  }

  return render(request, 'user/updateUser.html', context)

def deleteUser (request: HttpRequest, id):
  user = User.objects.get(id=id)
  user.delete()

  return redirect('/administrator/users/')
    
    