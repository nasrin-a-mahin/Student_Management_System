
from django.http import HttpResponseForbidden

from functools import wraps
# -----------------------------
# Role-based access decorator
# -----------------------------




def role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):

            print("Required role:", role)
            print("User role:", getattr(request.user.profile, 'role', None))
            print("Is superuser:", request.user.is_superuser)

            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)

            if request.user.profile.role == role:
                return view_func(request, *args, **kwargs)

            return HttpResponseForbidden("You are not allowed here")

        return _wrapped_view
    return decorator
