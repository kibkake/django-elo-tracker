# Generated by Django 3.2.8 on 2021-12-07 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0018_auto_20211207_1839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='upcoming',
            old_name='game_date',
            new_name='date',
        ),
    ]
