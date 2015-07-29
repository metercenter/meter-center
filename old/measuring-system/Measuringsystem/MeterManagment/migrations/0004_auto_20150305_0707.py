# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MeterManagment', '0003_usergroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usergroup',
            name='user_id',
            field=models.CharField(max_length=24),
            preserve_default=True,
        ),
    ]
