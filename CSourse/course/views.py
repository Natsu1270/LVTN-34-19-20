from django.shortcuts import render, get_object_or_404
from .models import Course


def courses(request):
    context = dict()
    if request.GET.get('search') is None:
        all_courses = Course.objects.order_by('rate_score').all()
    else:
        search = request.GET.get('search')
        all_courses = Course.objects.filter(name__contains=search)
    context['courses'] = all_courses
    context['course_num'] = len(all_courses)

    return render(request, 'course/courses_show.html', context)


def course_detail(request, course_code):
    context = dict()
    course = get_object_or_404(Course, code=course_code)
    relates = Course.objects.order_by('rate_score').all()
    context['course'] = course
    context['courses'] = relates
    return render(request, 'course/course_detail.html', context)
