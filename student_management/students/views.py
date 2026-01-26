from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from accounts.decorators import role_required

@role_required('ADMIN')
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

@role_required('ADMIN')
def student_create(request):
    if request.method == 'POST':
        Student.objects.create(
            user_id=request.POST['user'],
            roll_no=request.POST['roll_no'],
            date_of_birth=request.POST['dob'],
            course=request.POST['course'],
            year=request.POST['year']
        )
        return redirect('student_list')
    return render(request, 'students/student_form.html')

@role_required('ADMIN')
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.roll_no = request.POST['roll_no']
        student.course = request.POST['course']
        student.year = request.POST['year']
        student.save()
        return redirect('student_list')
    return render(request, 'students/student_form.html', {'student': student})

@role_required('ADMIN')
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')
