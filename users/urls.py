from django.urls import path

from .views import *

urlpatterns = [
    path('register/', register_user, name='register-user'),
    path('login/', MyTokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('profile/', get_user_profile, name='get-user-profile'),
    path('profile/update/', update_user_profile, name='update-user-profile'),
    path('', get_users, name='get-users'),
]
