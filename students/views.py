from email import message
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import user_passes_test
from .models import Student, Course
from .forms import StudentForm, CourseForm

@user_passes_test(lambda u: u.is_superuser)
def students(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    context = {
        'students': students,
        'courses': courses,
    }
    return render(request, 'students/students.html', context)

@user_passes_test(lambda u: u.is_superuser)
def new_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:students')
    else:
        form = StudentForm()
    return render(request, 'students/new_student.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def update_student(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students:landing_page')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/update_student.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def delete_student(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return render(request, 'partials/studentsTable.html', {'students': Student.objects.all()})

@user_passes_test(lambda u: u.is_superuser)
def courses(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'students/courses.html', context)

@user_passes_test(lambda u: u.is_superuser)
def new_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:courses')
    else:
        form = CourseForm()
    return render(request, 'students/new_course.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def update_course(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('students:courses')
    else:
        form = CourseForm(instance=course)
    return render(request, 'students/update_course.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def delete_course(request, pk):
    course = Course.objects.get(pk=pk)
    course.delete()
    return render(request, 'partials/coursesTable.html', {'courses': Course.objects.all()})

