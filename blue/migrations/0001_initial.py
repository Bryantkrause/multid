# Generated by Django 4.1.4 on 2022-12-09 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('content', models.CharField(max_length=50, verbose_name='title')),
                ('app_name', models.CharField(max_length=50, verbose_name='title')),
            ],
        ),
    ]
