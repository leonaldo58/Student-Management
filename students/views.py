from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm 

def home(request):
    return HttpResponse('<h1>Welcome to the home page</h1>')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students' : students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(isntance=student)
    return render(request, 'students/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(student, pk=pk)
    if request.method =='POST':
        Student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})