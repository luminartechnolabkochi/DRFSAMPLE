# Generated by Django 5.0 on 2024-03-22 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('director', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('run_time', models.IntegerField()),
                ('language', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
            ],
        ),
    ]
