from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from functools import wraps
# -----------------------------
# Role-based access decorator
# -----------------------------



def role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.profile.role == role:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("You are not allowed here")
        return _wrapped_view
    return decorator

# -----------------------------
# Dashboard redirect after login
# -----------------------------
@login_required
def dashboard_redirect(request):
    role = request.user.profile.role
    if role == 'ADMIN':
        return redirect('admin_dashboard')
    elif role == 'TEACHER':
        return redirect('teacher_dashboard')
    elif role == 'STUDENT':
        return redirect('student_dashboard')
    else:
        return redirect('login')

# -----------------------------
# Dashboards per role
# -----------------------------
@login_required
@role_required('ADMIN')
def admin_dashboard(request):
    # Add any context you want here
    context = {}
    return render(request, 'admin_dashboard.html', context)

@login_required
@role_required('TEACHER')
def teacher_dashboard(request):
    context = {}
    return render(request, 'teacher_dashboard.html', context)

@login_required
@role_required('STUDENT')
def student_dashboard(request):
    context = {}
    return render(request, 'student_dashboard.html', context)


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redirect based on role
            if user.is_superuser:
                return redirect('admin_dashboard')
            elif hasattr(user, 'teacherprofile'):
                return redirect('teacher_dashboard')
            else:
                return redirect('student_dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login.html')
