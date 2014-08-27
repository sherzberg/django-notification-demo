import json

from django.core import serializers

from notification import backends

from .models import Message


class HistoricalMessagesBackend(backends.BaseBackend):
    spam_sensitivity = 0

    def can_send(self, user, notice_type):
        return True

    def can_deliver(self, user, notice_type):
        return True

    def deliver(self, recipient, sender, notice_type, extra_context):
        c = self.default_context()
        context = {}
        context['base_url'] = c['base_url']

        for key, value in extra_context.iteritems():
            if hasattr(value, '_meta'):
                context[key] = json.loads(serializers.serialize('json', [value]))
            else:
                context[key] = value

        Message.objects.create(
            notice_label=notice_type.label,
            notice_display=notice_type.display,
            recipient=recipient,
            sender=sender,
            context=context
        )

