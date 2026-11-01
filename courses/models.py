from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator


class Course(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "پیش‌نویس"
        PUBLISHED = "published", "منتشرشده"

    title = models.CharField(
        max_length=200,
        verbose_name="عنوان دوره",
    )
    description = models.TextField(
        verbose_name="توضیحات دوره",
    )
    teacher = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="courses_taught",
        limit_choices_to={"role": "teacher"},
        verbose_name="استاد",
    )
    capacity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="ظرفیت دوره",
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="قیمت دوره",
    )
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT,
        verbose_name="وضعیت دوره",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد",
    )
    start_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="تاریخ شروع دوره",
    )

    end_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="تاریخ پایان دوره",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "دوره آموزشی"
        verbose_name_plural = "دوره‌های آموزشی"
        ordering = ["-created_at"]

class Session(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="sessions",
        verbose_name="دوره آموزشی",
    )
    title = models.CharField(
        max_length=200,
        verbose_name="عنوان جلسه",
    )
    description = models.TextField(
        blank=True,
        verbose_name="توضیحات جلسه",
    )
    date = models.DateField(
        verbose_name="تاریخ برگزاری",
    )
    order = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="ترتیب جلسه",
    )

    class Meta:
        verbose_name = "جلسه"
        verbose_name_plural = "جلسات"
        ordering = ["order"]
        constraints = [
            models.UniqueConstraint(
                fields=["course", "order"],
                name="unique_session_order_per_course",
            )
        ]

    def __str__(self):
        return f"{self.course.title} - {self.title}"