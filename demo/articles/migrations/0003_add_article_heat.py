# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import heatindex.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_create_fake_articles'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-heat',)},
        ),
        migrations.AddField(
            model_name='article',
            name='heat',
            field=heatindex.fields.HeatIndexField(default=1, score_field=('upvotes', 'downvotes'), timestamp_field='posted', db_index=True),
        ),
    ]
