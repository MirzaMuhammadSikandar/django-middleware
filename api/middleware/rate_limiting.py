import time
from enum import Enum
from django.core.cache import cache
from django.http import JsonResponse


class UserRole(Enum):
    GOLD = "gold"
    SILVER = "silver"
    BRONZE = "bronze"
    UNAUTHENTICATED = "unauthenticated"


class SkipPaths(Enum):
    REGISTER = "/api/users/register/"
    LOGIN = "/api/users/login/"
    ADMIN_LOGIN = "/admin/login/"
    ADMIN = "/admin/"


RATE_LIMITS = {
    UserRole.GOLD: 10,
    UserRole.SILVER: 5,
    UserRole.BRONZE: 2,
    UserRole.UNAUTHENTICATED: 1,
}


class RateLimitingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("-- RateLimitingMiddleware triggered --")  

        if any(request.path.startswith(path.value) for path in SkipPaths):
            print("Skipping rate limiting for:", request.path)
            return self.get_response(request)

        user = getattr(request, "user", None)
        ip = request.META.get("REMOTE_ADDR")
        identifier = ip

        if user and user.is_authenticated:
            identifier = str(user.id)
            role_str = getattr(user, "role", UserRole.BRONZE.value)
            role = UserRole(role_str) if role_str in UserRole._value2member_map_ else UserRole.BRONZE
        else:
            role = UserRole.UNAUTHENTICATED

        allowed_requests = RATE_LIMITS.get(role, 1)
        key = f"rl:{identifier}"
        data = cache.get(key, {"count": 0, "timestamp": time.time()})

        print(f"Redis Key: {key}, Data: {data}") 

        if time.time() - data["timestamp"] > 60:
            data = {"count": 0, "timestamp": time.time()}

        if data["count"] >= allowed_requests:
            print("Rate limit exceeded for:", identifier) 
            return JsonResponse(
                {"detail": f"Rate limit exceeded for role: {role.value}"}, status=429
            )

        data["count"] += 1
        cache.set(key, data, timeout=60)
        print(f"Updated Redis key {key} with count {data['count']}")

        return self.get_response(request)

