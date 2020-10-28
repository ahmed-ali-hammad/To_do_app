from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_view, name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),
    
]
