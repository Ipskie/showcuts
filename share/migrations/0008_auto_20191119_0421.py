# Generated by Django 2.2.6 on 2019-11-19 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0007_auto_20191119_0407'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shortcut',
            old_name='actions_blocks',
            new_name='action_blocks',
        ),
    ]
