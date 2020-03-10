# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_auto_20200306_1050'),
        ('shopapp', '0043_remove_product_categorynew'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_new',
            field=models.ForeignKey(related_name='shopproduct', blank=True, to='categories.Category', null=True),
        ),
    ]
