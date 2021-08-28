from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class TypeUserChoice(models.TextChoices):
        ADMIN = 'admin'
        SPECIALIST = 'specialist'
        PERSONAL_CABINET = 'personal_cabinet'

    type_user = models.CharField(max_length=128,
                                choices=TypeUserChoice.choices,
                                default = TypeUserChoice.PERSONAL_CABINET)
    name = models.CharField(max_length=128, null=True, blank=True)
    