import time
from django.core.cache import cache
from django.http import JsonResponse

RATE_LIMITS = {
    "gold": 10,
    "silver": 5,
    "bronze": 2,
    "unauthenticated": 1,
}

SKIP_RATE_LIMIT_PATHS = ["/api/register/", "/admin/login/", "/admin/"]


class RateLimitingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # ✅ Skip rate limiting
        if request.path in SKIP_RATE_LIMIT_PATHS:
            return self.get_response(request)

        user = getattr(request, "user", None)
        ip = request.META.get("REMOTE_ADDR")
        identifier = ip

        if user and user.is_authenticated:
            identifier = str(user.id)
            role = getattr(user, "role", "bronze")
        else:
            role = "unauthenticated"

        allowed_requests = RATE_LIMITS.get(role, 1)
        key = f"rl:{identifier}"
        data = cache.get(key, {"count": 0, "timestamp": time.time()})

        if time.time() - data["timestamp"] > 60:
            data = {"count": 0, "timestamp": time.time()}

        if data["count"] >= allowed_requests:
            return JsonResponse(
                {"detail": f"Rate limit exceeded for role: {role}"}, status=429
            )

        data["count"] += 1
        cache.set(key, data, timeout=60)
        return self.get_response(request)
    
