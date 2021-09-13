# Generated by Django 3.2.6 on 2021-09-13 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('death_date', models.DateField(blank=True, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
            ],
        ),
    ]