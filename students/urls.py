
from importlib.resources import path

from django.urls import path
from .views import students, new_student, update_student,delete_student, courses, new_course, update_course, delete_course

app_name = 'students'

urlpatterns = [
  path('', students, name='students'),
  path('students/', students, name='students'),

  path('new_student/', new_student, name='new_student'),
  path('update_student/<int:pk>', update_student, name='update_student'),
  path('delete_student/<int:pk>', delete_student, name='delete_student'),
  path('courses/', courses, name='courses'),
  path('new_course/', new_course, name='new_course'),
  path('update_course/<int:pk>', update_course, name='update_course'),
  path('delete_course/<int:pk>', delete_course, name='delete_course'),

]
