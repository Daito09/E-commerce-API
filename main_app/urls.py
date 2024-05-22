from django.urls import path
from . import views

urlpatterns=[
    path('students', views.StudentEndpoint.as_view(), name='student'),
    path('students/<int:pk>', views.StudentDetailEndpoint.as_view(), name='student')
]