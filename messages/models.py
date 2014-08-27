from django.db import models

from jsonfield.fields import JSONField


class Message(models.Model):
    date_added = models.DateTimeField(auto_now_add=True, auto_now=False)
    notice_label = models.CharField(max_length=100, null=False, blank=False)
    notice_display = models.CharField(max_length=100, null=False, blank=False)
    recipient = models.CharField(max_length=100, null=False, blank=False)
    sender = models.CharField(max_length=100, null=True, blank=True)

    read = models.BooleanField(default=False)

    context = JSONField()
