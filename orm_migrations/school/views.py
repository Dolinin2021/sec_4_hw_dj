from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    ordering = 'group'
    template = 'school/students_list.html'
    student_list = Student.objects.all().order_by(ordering).prefetch_related('teacher')
    context = {
        'object_list': student_list
    }
    return render(request, template, context)