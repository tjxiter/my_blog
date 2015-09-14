# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_remove_tag_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='article',
            field=models.ForeignKey(default="11", to='article.Article'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tag',
            name='num',
            field=models.IntegerField(default=0),
        ),
    ]
