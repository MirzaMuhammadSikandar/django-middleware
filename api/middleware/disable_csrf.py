from django.utils.deprecation import MiddlewareMixin

class DisableCSRFMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path in ['/api/users/register/', '/api/users/login/']:
            setattr(request, '_dont_enforce_csrf_checks', True)
            
