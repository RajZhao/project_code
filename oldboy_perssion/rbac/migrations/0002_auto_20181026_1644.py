# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-26 08:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='role',
            new_name='roles',
        ),
    ]
