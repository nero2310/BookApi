# Generated by Django 3.2.6 on 2021-10-11 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google_book_api', '0002_library'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='library',
            name='books',
        ),
        migrations.AddField(
            model_name='library',
            name='books',
            field=models.ManyToManyField(to='google_book_api.Book'),
        ),
    ]
