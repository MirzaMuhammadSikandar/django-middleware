from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ItemViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')  
router.register(r'items', ItemViewSet, basename='item')  

urlpatterns = [
    path('api/', include(router.urls)),  
]