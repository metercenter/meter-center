# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MeterManagment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_password',
            field=models.CharField(default='123456', max_length=10, blank=True),
            preserve_default=False,
        ),
    ]
