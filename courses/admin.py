
from django.contrib import admin

from .models import Course, Session


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "teacher",
        "capacity",
        "price",
        "status",
        "start_date",
        "end_date",
        "created_at",
    )
    list_filter = ("status", "created_at")
    search_fields = ("title", "description", "teacher__username")
    ordering = ("-created_at",)


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "date", "order")
    list_filter = ("course", "date")
    search_fields = ("title", "course__title")
    ordering = ("course", "order")