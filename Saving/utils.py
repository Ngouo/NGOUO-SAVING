import logging
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)

def notification(subject="Nouvelle opération", message="Une nouvelle opération a été enregistrée. Veuillez consulter la plateforme pour plus d'informations."):
    User = get_user_model()
    recipients = [user.email for user in User.objects.filter(is_active=True) if user.email]

    if not recipients:
        logger.warning("Aucun destinataire trouvé pour la notification.")
        return

    try:
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=recipients,
        )
        email.send(fail_silently=False)
        logger.info(f"Notification envoyée à {len(recipients)} utilisateurs.")
    except Exception as e:
        logger.error(f"Erreur lors de l’envoi de la notification : {str(e)}")