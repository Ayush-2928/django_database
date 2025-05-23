# Generated by Django 5.2 on 2025-04-11 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('enroll', models.CharField(max_length=20, unique=True)),
                ('age', models.PositiveIntegerField()),
                ('branch', models.CharField(max_length=50)),
            ],
        ),
    ]
