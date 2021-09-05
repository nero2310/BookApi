# Generated by Django 3.2.6 on 2021-08-30 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('kind', models.CharField(blank=True, max_length=100)),
                ('api_book_id', models.CharField(blank=True, max_length=100)),
                ('authors', models.JSONField()),
                ('publisher', models.CharField(blank=True, max_length=200)),
                ('publish_data', models.DateField(blank=True, null=True)),
            ],
        ),
    ]