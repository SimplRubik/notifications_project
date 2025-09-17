from django.db import models

class Notification(models.Model):
    CHANNELS = [
        ('email', 'Email'),
        ('sms', 'SMS'),
        ('telegram', 'Telegram'),
    ]
    user = models.CharField(max_length=100)
    message = models.TextField()
    channels = models.JSONField(default=list)
    status = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    