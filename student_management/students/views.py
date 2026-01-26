from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from accounts.decorators import role_required
from django.contrib.auth.decorators import login_required
@role_required('ADMIN')
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

@login_required
@role_required('ADMIN')
def student_create(request):
    if request.method == 'POST':
        Student.objects.create(
            roll_no=request.POST['roll_no'],
            name=request.POST['name'],
            email=request.POST['email'],
            course=request.POST['course'],
        )
        return redirect('student_list')

    return render(request, 'students/student_form.html')


@login_required
@role_required('ADMIN')
def student_update(request, pk):
    student = Student.objects.get(pk=pk)

    if request.method == 'POST':
        student.roll_no = request.POST['roll_no']
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.course = request.POST['course']
        student.save()
        return redirect('student_list')

    return render(request, 'students/student_form.html', {
        'student': student
    })


@role_required('ADMIN')
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')
