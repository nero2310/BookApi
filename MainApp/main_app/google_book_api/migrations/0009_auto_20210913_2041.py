# Generated by Django 3.2.6 on 2021-09-13 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        ('google_book_api', '0008_auto_20210907_2059'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='authors.Author'),
        ),
    ]