from django.urls import path
from .views import SignupView


from .views import *


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('sleep-assessment/', SleepAssessmentView.as_view(), name='sleep-assessment'),
]
