from django.core.mail import send_mail
from django.template.loader import render_to_string

def send_authentication_token(user, token):
    subject = 'Token de Autenticación de Doble Factor'
    template_name = 'authentication_token_email.html'
    context = {'user': user, 'token': token}
    html_message = render_to_string(template_name, context)
    
    send_mail(
        subject,
        None,
        'Sistema de Seguridad UNFV',
        [user.email],
        html_message=html_message,
    )


def email_carta(user):
    subject = 'Token de Autenticación de Doble Factor'
    message = f'Tu token de autenticación de doble factor es:'
    from_email = 'Sistema de Seguridad UNFV'
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)