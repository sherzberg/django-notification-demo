# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('notice_label', models.CharField(max_length=100)),
                ('notice_display', models.CharField(max_length=100)),
                ('recipient', models.CharField(max_length=100)),
                ('sender', models.CharField(max_length=100, null=True, blank=True)),
                ('read', models.BooleanField(default=False)),
                ('context', jsonfield.fields.JSONField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
