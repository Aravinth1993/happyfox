from django.db import models

class Email(models.Model):
    from_address = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    received_datetime = models.DateTimeField()
    is_read = models.BooleanField(default=False)

