from django.shortcuts import render
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView
from .forms import CustomUserSignupForm


class SignUpView(BSModalCreateView):
    form_class = CustomUserSignupForm
    template_name = 'accounts/signup.html'
    success_message = 'Success: Sign up succeeded!'
    success_url = reverse_lazy('')
