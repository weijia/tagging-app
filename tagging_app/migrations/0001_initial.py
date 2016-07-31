# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tagging', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_app', models.CharField(help_text='Tag creator', max_length=50, null=True, verbose_name='Tag creator', blank=True)),
                ('tagged_item', models.ForeignKey(related_name='tagged_item', verbose_name='tagged_item', to='tagging.TaggedItem')),
                ('user', models.ForeignKey(related_name='tagging_user', verbose_name='tagging_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
