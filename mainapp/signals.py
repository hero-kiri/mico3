from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from .models import Email, PushMessage

@receiver(post_save, sender=PushMessage)
def send_push_message(sender, instance, created, **kwargs):
    if created:
        emails = Email.objects.values_list('email', flat=True)  # ['email', 'email']
        subject = 'Новое сообщение от Мико Медикал'
        message = instance.message 
        from_email = 'hero.beka@gmail.com'
        
        for email in emails:
            recipient_list = [email]
            # Отправка сообщения на почту всем пользователям из базы данных
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        
        print('Сообщение отправлено на почту всем пользователям')
        