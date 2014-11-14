# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from heatindex.utils import update_heat_column_migration_factory


def null_function(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_heat_column'),
    ]

    operations = [
        migrations.RunPython(update_heat_column_migration_factory("articles", "Article", "heat"), null_function)
    ]
