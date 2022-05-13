from django.conf import settings
from django.db import models


class Userdetails(models.Model):
    "Generated Model"
    user = models.BigIntegerField()
    email = models.BigIntegerField(
        null=True,
        blank=True,
    )
    password = models.BigIntegerField(
        null=True,
        blank=True,
    )


# Create your models here.
