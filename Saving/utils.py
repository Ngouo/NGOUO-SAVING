from django.core.mail import send_mass_mail
from django.contrib.auth.models import User

def notification():
    users = User.objects.filter(is_active=True).exclude(email='')

    emails = [
        ("Notification NGOUO Saving",
          "Une opération vient d'etre effectué dans la caisse de la famille NGOUO. Veuillez consulter la palateforme pour plus de détails.", 
          "ton_email@example.com",
            [user.email])
        for user in users
    ]

    send_mass_mail(emails, fail_silently=False)