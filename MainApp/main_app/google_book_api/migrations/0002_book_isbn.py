# Generated by Django 3.2.6 on 2021-09-05 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google_book_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, max_length=13),
        ),
    ]