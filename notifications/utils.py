from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import Client
from telegram import Bot

def send_email(to_email, message):
    try:
        # Для теста 
        send_mail(
            subject='Уведомление',
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[to_email],
            fail_silently=False,
        )
        print(f"[EMAIL] Письмо успешно отправлено на {to_email}")
        return True
    except Exception as e:
        print(f"[EMAIL] Ошибка при отправке Email: {e}")
        return False

def send_sms(to_phone, message):
    try:
        # Для теста
        print(f"[SMS] To: {to_phone}, Message: {message}")
        return True
    except Exception as e:
        print(f"[SMS] Ошибка при отправке SMS: {e}")
        return False

def send_telegram(telegram_id, message):
    try:
        # Для теста
        print(f"[Telegram] To: {telegram_id}, Message: {message}")
        return True
    except Exception as e:
        print(f"[Telegram] Ошибка при отправке Telegram: {e}")
        return False

def notify_user(user_email=None, user_phone=None, user_telegram=None, message=""):
    
    if user_email and send_email(user_email, message):
        return "Отправлено по Email"
    if user_phone and send_sms(user_phone, message):
        return "Отправлено по SMS"
    if user_telegram and send_telegram(user_telegram, message):
        return "Отправлено по Telegram"
    return "Не удалось отправить уведомление"

