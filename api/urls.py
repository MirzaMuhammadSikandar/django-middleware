from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ItemCreateView, ItemListView

urlpatterns = [
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),
    path("logout/", LogoutView.as_view()),
    path('items/', ItemListView.as_view()),    
    path('items/create/', ItemCreateView.as_view()),  
]

