# Generated by Django 3.2.6 on 2021-11-07 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('google_book_api', '0003_auto_20211011_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
