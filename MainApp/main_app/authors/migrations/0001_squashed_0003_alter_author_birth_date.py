# Generated by Django 3.2.6 on 2021-09-13 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('authors', '0001_initial'), ('authors', '0002_author_slug'), ('authors', '0003_alter_author_birth_date')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('death_date', models.DateField(blank=True, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(default='abc', unique=True)),
            ],
        ),
    ]
