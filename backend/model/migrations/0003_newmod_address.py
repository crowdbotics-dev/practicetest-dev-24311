# Generated by Django 2.2.26 on 2022-05-03 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_newmod_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='newmod',
            name='address',
            field=models.TimeField(blank=True, null=True),
        ),
    ]