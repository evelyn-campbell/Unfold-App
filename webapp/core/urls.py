from django.urls import path
from . import views

# add other paths here in a similar fashion
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]

