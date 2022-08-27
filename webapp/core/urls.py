from django.urls import path
from . import views

# add other paths here in a similar fashion
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/edit/avatar/', views.edit_avatar, name='edit_avatar'),
    path('profile/edit/password/', views.edit_password, name='edit_password'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/create_post/', views.create_post, name='create_post'),

]

