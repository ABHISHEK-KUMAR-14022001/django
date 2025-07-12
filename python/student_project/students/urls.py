from django.urls import path
from .views import student_form, success_page

urlpatterns = [
    path('', student_form, name='student_form'),
    path('success/', success_page, name='success'),
]
