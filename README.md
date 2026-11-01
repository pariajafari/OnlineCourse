# سامانه مدیریت دوره‌های آموزشی (OnlineCourse)

## معرفی پروژه
این پروژه یک سامانه مدیریت دوره‌های آموزشی است که با استفاده از Django و PostgreSQL توسعه داده می‌شود.

هدف سامانه، فراهم کردن بستری برای مدیریت دوره‌ها، جلسات آموزشی، ثبت‌نام دانشجویان و ارزیابی آن‌ها توسط استاد است.

## تکنولوژی‌های مورد استفاده
- Python
- Django
- PostgreSQL
- HTML, CSS, JavaScript (در مراحل توسعه رابط کاربری)

## ساختار پروژه

```text
OnlineCourse/
│
├── accounts/
├── courses/
├── enrollments/
├── config/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## پیش‌نیازها
برای اجرای پروژه به موارد زیر نیاز است:

- Python
- PostgreSQL
- Git

## راه‌اندازی پروژه

### ۱. دریافت پروژه

```bash
git clone REPOSITORY_URL
cd OnlineCourse
```

### ۲. ایجاد محیط مجازی

در ویندوز:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

در macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### ۳. نصب وابستگی‌ها

```bash
python -m pip install -r requirements.txt
```

### ۴. تنظیم دیتابیس

ابتدا PostgreSQL را نصب و اجرا کنید و یک دیتابیس با نام زیر بسازید:

```text
onlinecourse_db
```

سپس در پوشه اصلی پروژه، فایل `.env` ایجاد کنید و اطلاعات اتصال دیتابیس و کلید امنیتی Django را در آن قرار دهید.

نمونه ساختار فایل:

```env
SECRET_KEY=your-secret-key
DB_NAME=onlinecourse_db
DB_USER=postgres
DB_PASSWORD=your-database-password
DB_HOST=localhost
DB_PORT=5432
```

**توجه:** فایل `.env` شامل اطلاعات محرمانه است و نباید در GitHub قرار بگیرد.

### ۵. اجرای Migrationها

```bash
python manage.py migrate
```

### ۶. ساخت حساب مدیر

```bash
python manage.py createsuperuser
```

### ۷. اجرای سرور توسعه

```bash
python manage.py runserver
```

سپس پنل مدیریت از طریق آدرس زیر قابل دسترسی است:

http://127.0.0.1:8000/admin/

## اپلیکیشن‌های پروژه

- **accounts:** مدیریت حساب‌های کاربری و نقش کاربران
- **courses:** مدیریت دوره‌های آموزشی و جلسات
- **enrollments:** مدیریت ثبت‌نام دانشجویان در دوره‌ها و ارزیابی آن‌ها

## وضعیت توسعه

پروژه در حال توسعه است و امکانات آن مطابق مراحل تعریف‌شده در پروژه دانشگاهی تکمیل خواهد شد.