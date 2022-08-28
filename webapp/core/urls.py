from django.urls import path
from . import views

# add other paths here in a similar fashion
urlpatterns = [
    # home/index page
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload-status/', views.upload_status, name='upload-status'),
    #path('like-post/', views.like_post, name='like-post'),

    # authentication paths
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),

    # profile paths
    path('profile/', views.profile, name='profile'),
    path('profile/<str:pk>/', views.other_profile, name='other_profile'),
    path('settings/', views.settings, name='settings'),

    # group and friend paths
    path('groups/', views.groups, name='groups'),
    #path('groups/<int:group_id>/', views.group_detail, name='group_detail'),
    #path('groups/<int:group_id>/edit/', views.edit_group, name='edit_group'),
    path('friends/', views.friends, name='friends'),
    path('friends/request_accepted/<str:pk>', views.recieve_friend_request, name='request_accepted'),
    #path('friends/<int:friend_id>/', views.friend_detail, name='friend_detail'),


]

