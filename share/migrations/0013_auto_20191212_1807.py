# Generated by Django 2.2.7 on 2019-12-12 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0012_auto_20191129_1640'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shortcut',
            options={'ordering': ['-created_on']},
        ),
        migrations.AddField(
            model_name='shortcut',
            name='workflow_version',
            field=models.IntegerField(default=0, verbose_name='Workflow Version'),
        ),
    ]
