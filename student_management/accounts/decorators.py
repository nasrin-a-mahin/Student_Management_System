
from django.http import HttpResponseForbidden

from functools import wraps
# -----------------------------
# Role-based access decorator
# -----------------------------




from django.http import HttpResponseForbidden
from functools import wraps

def role_required(*roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):

            print("Allowed roles:", roles)
            print("User role:", getattr(request.user.profile, 'role', None))
            print("Is superuser:", request.user.is_superuser)

            # Always allow superuser
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)

            # Allow if user's role is in allowed roles
            if request.user.profile.role in roles:
                return view_func(request, *args, **kwargs)

            return HttpResponseForbidden("You are not allowed here")
        return _wrapped_view
    return decorator
