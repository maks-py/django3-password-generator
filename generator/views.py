from django.shortcuts import render
from django.http import HttpResponse
import random
from datetime import datetime


# Create your views here.
def home(request):
  return render(request, 'generator/home.html')

def password(request):

  chars = list('abcdefghijklmnopqrstuvwxyz')
  length = int(request.GET.get('length', '12'))
  thepassword = ''

  if request.GET.get('uppercase'):
    chars.extend(list('ABCDEFGHIJLMNOPQRSTUVWXYZ'))

  if request.GET.get('special'):
    chars.extend(list('~!@#$%^&*()_+|?`'))
 
  if request.GET.get('numbers'):
    chars.extend(list('0123456789'))

  for x in range(length):
    thepassword += random.choice(chars)

  return render(request, 'generator/password.html', {'password' : thepassword})


def about(request):
  dt = datetime.now()
  datetimestr = dt.ctime()
  return render(request, 'generator/about.html', {'datetime' : datetimestr})