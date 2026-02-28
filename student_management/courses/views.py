from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from students.models import Student
from django.contrib.auth.decorators import login_required
from accounts.decorators import role_required

@login_required
@role_required('ADMIN')
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


@login_required
@role_required('ADMIN')
def course_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Course.objects.create(name=name)
        return redirect('course_list')
    return render(request, 'courses/course_form.html')


@login_required
@role_required('ADMIN')
def assign_students(request, pk):
    course = get_object_or_404(Course, pk=pk)
    students = Student.objects.all()

    if request.method == 'POST':
        selected_students = request.POST.getlist('students')
        course.students.set(selected_students)
        return redirect('course_list')

    return render(request, 'courses/assign_students.html', {
        'course': course,
        'students': students
    })
