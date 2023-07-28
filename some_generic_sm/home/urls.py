from django.urls import path
from some_generic_sm.home.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]