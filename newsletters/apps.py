from django.apps import AppConfig
from django.db.models.signals import post_migrate

from notification import models as notification


def create_notice_types(sender, **kwargs):
    notification.create_notice_type('newsletters:new_newsletter', 'New Newsletter', '')
    notification.create_notice_type('newsletters:weekly_recap', 'Weekly Recap', '')


class NewslettersConfig(AppConfig):
    name = 'newsletters'
    verbose_name = 'newsletters'

    def ready(self, *args, **kwargs):
        post_migrate.connect(create_notice_types, sender=self)
