from django.http import JsonResponse
from django.conf import settings
from functools import wraps

def require_api_key(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        if api_key not in settings.API_KEYS:
            return JsonResponse({"error": "INVALID_API_KEY", "message": "Missing or invalid API key"}, status=401)
        return view_func(request, *args, **kwargs)
    return _wrapped_view
