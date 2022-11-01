from django.template import loader
from django.http import HttpResponse

def index(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())

def users(request):
  template = loader.get_template('users.html')
  return HttpResponse(template.render())