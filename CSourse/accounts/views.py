from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.http import require_http_methods, require_POST
from .forms import SignUpForm, LoginForm
from .models import User
from role.models import Role

from django.utils import timezone


@require_http_methods(["GET", "POST"])
def user_connect(request):
    sign_up_form = SignUpForm()
    log_in_form = LoginForm()
    if request.method == 'POST':
        if request.POST.get('submit') == 'signup':
            sign_up_form = SignUpForm(request.POST)
            if sign_up_form.is_valid():
                username = sign_up_form.cleaned_data.get('username')
                email = sign_up_form.cleaned_data.get('email')
                password = sign_up_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('homepage')
            else:
                sign_up_form = SignUpForm()
        else:
            log_in_form = LoginForm(request.POST)
            if log_in_form.is_valid():
                username = log_in_form.cleaned_data.get('username')
                password = log_in_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('homepage')
            else:
                return {'result': 5}
    return render(request, 'accounts/signup.html', {'log_in_form': log_in_form, 'sign_up_form': sign_up_form})


@require_POST
def log_in(request):
    if request.method == 'POST':
        response = dict()
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if not user:
            response['code'] = 404
            response['message'] = "Cannot log in, please check your informations !"
            response['result'] = None
        elif not user.check_password(password):
            response['code'] = 404
            response['message'] = "Incorrect password"
            response['result'] = None
        elif not user.is_active:
            response['code'] = 404
            response['message'] = "This user is no longer active"
            response['result'] = None
        elif user:
            response['code'] = 200
            response['message'] = "Login successfully"
            response['result'] = serializers.serialize('json', [user])
            login(request, user)

        return JsonResponse(response)


@require_POST
def sign_up(request):
    if request.method == 'POST':
        response = dict()
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(email=email).count() > 0:
            response['code'] = 409
            response['message'] = "This email is already used to register"
            response['result'] = None
        elif User.objects.filter(username=username).count() > 0:
            response['code'] = 409
            response['message'] = "This username is already used to register"
            response['result'] = None
        else:
            student_role = Role()
            try:
                student_role = Role.objects.get(name='student')
            except Role.DoesNotExist:
                student_role = Role.objects.create(
                    name='student', created_date=timezone.now(), description='Student role'
                )
            user = User.objects.create_user(username, email, password)
            user.roles.add(student_role)
            user.save()
            login(request, user)
            response['code'] = 200
            response['message'] = "Register successfully"
            response['result'] = serializers.serialize('json', [user])

        return JsonResponse(response)


def log_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage')
