# Generated by Django 2.2.26 on 2022-05-31 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("practicetest", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userdetails",
            name="team",
            field=models.TextField(blank=True, null=True),
        ),
    ]
