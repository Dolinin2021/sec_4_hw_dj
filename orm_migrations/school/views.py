from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    ordering = 'group'
    student_list = Student.objects.all().order_by(ordering).prefetch_related('teacher')
    print(student_list)
    template = 'school/students_list.html'
    context = {
        'object_list': student_list
    }
    return render(request, template, context)
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by