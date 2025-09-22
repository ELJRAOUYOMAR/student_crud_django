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
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)  # This line was correct
        if form.is_valid():
            # Instead of manually creating the student, just save the form
            form.save()  # This handles the file upload properly
            return render(request, "add.html", {'form': StudentForm(), 'success': True})
        else:
            # If form is not valid, show errors
            return render(request, 'add.html', {'form': form})
    else:
        form = StudentForm()
    return render(request, 'add.html', {'form': form})

def edit(request,id):
    student=Student.objects.get(pk=id)
    if request.method=='POST':
        form=StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return render(request,'edit.html',{'form':form,'success':True})
        else:
            return render(request, 'edit.html', {'form': form})
    else:
        form=StudentForm(instance=student)
    return render(request,'edit.html',{'form':form})


def delete(request,id):
    if request.method=='POST':
        student=Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))
    