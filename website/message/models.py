from django.db import models

# Create your models here.


class Message(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sender = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="Sender")
    recipient = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="Receiver")

    def __str__(self):
        return self.subject
