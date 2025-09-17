from celery import shared_task
from .models import Notification

@shared_task
def send_notification(notification_id):
    notification = Notification.objects.get(id=notification_id)
    for channel in notification.channels:
        try:
            if channel == 'email':
                notification.status['email'] = 'success'

            elif channel == 'sms':
                notification.status['sms'] = 'success'
            
            elif channel == 'telegram':
                notification.status['telegram'] = 'success'
        
        except Exception as e:
            notification.status[channel] = f'failed: {str(e)}'
    
    notification.save()
            