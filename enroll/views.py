from django.shortcuts import render, HttpResponseRedirect
from .models import User

from .forms import Studentinfo

# Create your views here.
def addshow(request):
    if request.method=='POST':
     fm=Studentinfo(request.POST)
     if fm.is_valid():
         fm.save()
         fm=Studentinfo()
    else:
     fm=Studentinfo()
    stud=User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu':stud})


    #This is delete function

def delete_data(request,id):
        if request.method == 'POST':
            pi=User.objects.get(pk=id)
            pi.delete
            return HttpResponseRedirect('/')

#This for function update

def update_data(request,id):
    if request.method== 'POST':
        pi= User.objects.get(pk=id)
        fm=Studentinfo(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
            pi= User.objects.get(pk=id)
            fm=Studentinfo(request.POST)
    return render(request, 'enroll/updatestudent.html', {'form':fm})