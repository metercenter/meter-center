# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datahandle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_id',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
