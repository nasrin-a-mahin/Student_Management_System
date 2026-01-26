from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from functools import wraps
from accounts.decorators import role_required
# -----------------------------
# Role-based access decorator
# -----------------------------




# def role_required(role):
#     def decorator(view_func):
#         @wraps(view_func)
#         def _wrapped_view(request, *args, **kwargs):

#             print("Required role:", role)
#             print("User role:", getattr(request.user.profile, 'role', None))
#             print("Is superuser:", request.user.is_superuser)

#             if request.user.is_superuser:
#                 return view_func(request, *args, **kwargs)

#             if request.user.profile.role == role:
#                 return view_func(request, *args, **kwargs)

#             return HttpResponseForbidden("You are not allowed here")

#         return _wrapped_view
#     return decorator

# -----------------------------
# Dashboard redirect after login
# -----------------------------
@login_required
def dashboard_redirect(request):

    # System admin always wins
    if request.user.is_superuser:
        return redirect('admin_dashboard')

    # Safety: profile must exist
    if not hasattr(request.user, 'profile'):
        return HttpResponseForbidden("Profile not found")

    role = request.user.profile.role
    print('role',role)
    if role == 'ADMIN':
        return redirect('admin_dashboard')

    elif role == 'TEACHER':
        return redirect('teacher_dashboard')

    elif role == 'STUDENT':
        return redirect('student_dashboard')

    # Catch invalid roles
    return HttpResponseForbidden("Invalid role assigned")


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
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard_redirect')  # ONLY THIS

        return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')
