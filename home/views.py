from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
   return render(request, 'pages/home.html')
def proc(request):
    return render(request,'pages/proc.html')
def dttdraw(request):
    return render(request,'pages/thanhcun.html')
def dttdrawabout(request): return render(request,'dttdraw/pages/thanhcunfull/test.html')
def dttdrawdino(request): return render(request,'dttdraw/pages/thanhcunfull/gamedino.html')
def webupdate(request):
    return render(request,  'pages/webupdatecongdo.html')
def contact(request):
   return render(request, 'pages/contact.html')
def error(request, exception):
    return render(request, 'pages/error.html', {'message': exception})
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})