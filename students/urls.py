from django.urls import path, include
from .views import student_data_api_view
urlpatterns = [
    path('student_data', student_data_api_view.as_view()),
]