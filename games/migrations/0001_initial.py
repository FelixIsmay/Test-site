# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0020_add_index_on_page_first_published_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameIndex',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, auto_created=True, parent_link=True, to='wagtailcore.Page', primary_key=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='GamePage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, auto_created=True, parent_link=True, to='wagtailcore.Page', primary_key=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
