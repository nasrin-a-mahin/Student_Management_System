from django.shortcuts import render, redirect
from students.models import Student
from .models import Attendance
from django.contrib.auth.decorators import login_required
from datetime import date
from accounts.decorators import role_required

@role_required('ADMIN', 'TEACHER')
@login_required
def mark_attendance(request):
    students = Student.objects.all()
    today = date.today()
    
    for student in students:
        print("Student ID:", student.id)

    if request.method == 'POST':
        for student in students:
            status = request.POST.get(str(student.id)) == 'on'
            Attendance.objects.update_or_create(
                student=student,
                date=today,
                defaults={'status': status}
            )
        return redirect('mark_attendance')

    return render(request, 'attendance/mark_attendance.html', {
        'students': students,
        'today': today
    })
@role_required('ADMIN', 'TEACHER')
@login_required
def attendance_list(request):
    records = Attendance.objects.select_related('student').order_by('-date')
    print('records',records);
    return render(request, 'attendance/attendance_list.html', {
        'records': records
    })
