from .models import User, Rol, VotationGroup
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
    

# groups
def groups(request):
  groups = VotationGroup.objects.all().values()

  context = {
    'groups' : groups
  }
  return render(request, 'votationGroups/groups.html', context)


def createGroup(request: HttpRequest):
  
  if(request.method == 'POST'):
    name = request.POST.get('name')
    description = request.POST.get('description')
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    active =  bool(request.POST.get('active')) 
       
    group = VotationGroup(name=name, description=description, start_date=start_date, end_date=end_date, active=active)
    group.save()
    return redirect('/administrator/groups/')

  return render(request, 'votationGroups/createGroup.html')


def updateGroup(request: HttpRequest, id):
  
  group = VotationGroup.objects.get(id=id)
  group.start_date = group.start_date.strftime("%Y-%m-%d")
  group.end_date = group.end_date.strftime("%Y-%m-%d")

  if(request.method == 'POST'):
    name = request.POST.get('name')
    description = request.POST.get('description')
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    active = request.POST.get('active')

    group.name = name
    group.description = description
    group.start_date = start_date
    group.end_date = end_date
    group.active = active
    group.save()

    return redirect('/administrator/groups/')

  context = {
    'group': group,
  }

  return render(request, 'votationGroups/updateGroup.html', context)


def deleteGroup (request: HttpRequest, id):
  group = VotationGroup.objects.get(id=id)
  group.delete()

  return redirect('/administrator/groups/')
    
        
    