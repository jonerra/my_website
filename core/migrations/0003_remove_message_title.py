# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20151023_2208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='title',
        ),
    ]
