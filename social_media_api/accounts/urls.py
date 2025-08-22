from django.urls import path
from .views import RegisterView, LoginView, ProfileView 
from .views import FollowUserView, UnfollowUserView, ListFollowersView, ListFollowingView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'), 
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),  # User profile view
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),  # Follow a user
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),  # Unfollow a user
    path('followers/', ListFollowersView.as_view(), name='list-followers'),  # List followers
    path('following/', ListFollowingView.as_view(), name='list-following'),  # List following
]