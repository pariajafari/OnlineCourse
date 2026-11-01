from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "student", "دانشجو"
        TEACHER = "teacher", "استاد"

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.STUDENT,
        verbose_name="نقش کاربر",
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
