from django.shortcuts import render, get_object_or_404
from .models import AbilityExam, Exam
from course.models import Course


def ability_exam(request, course_code):
    context = dict()
    course = get_object_or_404(Course, code=course_code)
    ability_exams = course.ability_exam.all()
    context['ability_exams'] = ability_exams
    context['course'] = course

    return render(request, 'exam/ability_exam.html', context)


def take_exam(request, exam_id):
    context = dict()
    exam = get_object_or_404(Exam, pk=exam_id)
    questions = exam.question_set.all()
    context['questions'] = questions
    return render(request, 'exam/take_exam.html', context)
