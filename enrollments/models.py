from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Enrollment(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="enrollments",
        limit_choices_to={"role": "student"},
        verbose_name="دانشجو",
    )

    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="enrollments",
        verbose_name="دوره",
    )

    enrolled_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ثبت‌نام",
    )

    score = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ],
        verbose_name="نمره",
    )

    feedback = models.TextField(
        blank=True,
        verbose_name="ارزیابی استاد",
    )

    class Meta:
        verbose_name = "ثبت‌نام"
        verbose_name_plural = "ثبت‌نام‌ها"

        constraints = [
            models.UniqueConstraint(
                fields=["student", "course"],
                name="unique_student_course_enrollment",
            )
        ]

    def __str__(self):
        return f"{self.student.username} - {self.course.title}"