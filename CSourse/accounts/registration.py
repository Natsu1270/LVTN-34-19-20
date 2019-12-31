from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from ..core.mail import mail_user
from .tokens import make_activation_token


def send_welcome_email(request, user:User):
    settings = request.settings

    mail_subject = _("Welcome to %(site_name)s!")
    mail_subject = mail_subject % {"site_name": settings.site_name}

    if not user.requires_activation
