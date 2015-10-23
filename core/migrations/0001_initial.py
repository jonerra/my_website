# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=300)),
                ('title', models.IntegerField(default=0, choices=[(0, b'Ms.'), (1, b'Mrs.'), (2, b'Mr.'), (3, b'Dr.')])),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=300)),
                ('message', models.TextField(null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
