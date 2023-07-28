from django.urls import path
from some_generic_sm.users.views import SignInView, SignUpView, SignOutView

urlpatterns = [
    path('user/signup/', SignUpView.as_view(), name='user_signup'),
    path('user/signin/', SignInView.as_view(), name='user_signin'),
    path('user/signout/', SignOutView.as_view(), name='user_signout'),
]