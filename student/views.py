from django.shortcuts import render
from .models import Student
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import StudentForm

# Create your views here.
def index(request):
    all_students=Student.objects.all()
    return render(request,"index.html",{'students':all_students})

def view_student(request,id):
    student=Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method=='POST':
        form=StudentForm(request.POST , request.FILES)
        if form.is_valid():
            new_number=form.cleaned_data["number"]
            new_first_name=form.cleaned_data["first_name"]
            new_last_name=form.cleaned_data["last_name"]
            new_email=form.cleaned_data["email"]
            new_note=form.cleaned_data["note"]
            new_photo=form.cleaned_data["photo"]
            
            new_student=Student(
                number=new_number,
                first_name=new_first_name,
                last_name=new_last_name,
                email=new_email,
                note=new_note,
                photo=new_photo
            )
                
            new_student.save()
            return render(request,"add.html",{'form':StudentForm(),'success':True})
    else:
        form=StudentForm()
    return render(request,'add.html',{'form':StudentForm()})

def edit(request,id):
    if request.method=='POST':
        student=Student.objects.get(pk=id)
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return render(request,'edit.html',{'form':form,'success':True})
    else:
        student=Student.objects.get(pk=id)
        form=StudentForm(instance=student)
    return render(request,'edit.html',{'form':form})


def delete(request,id):
    if request.method=='POST':
        student=Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))
    