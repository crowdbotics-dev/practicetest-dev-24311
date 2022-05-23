from django.conf import settings
from django.db import models


class Newmod(models.Model):
    "Generated Model"
    name = models.BigIntegerField()
    email = models.TextField(
        null=True,
        blank=True,
    )
    address = models.TimeField(
        null=True,
        blank=True,
    )


# Create your models here.
