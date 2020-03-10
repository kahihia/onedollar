# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20170217_1111'),
        ('shopapp', '0041_auto_20170811_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categorynew',
            field=models.ForeignKey(related_name='shopproduct', blank=True, to='categories.Category', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(related_name='shopproduct', blank=True, to='onedollar.Category', null=True),
        ),
    ]
