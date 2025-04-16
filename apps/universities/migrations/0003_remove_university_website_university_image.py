# Generated by Django 5.1.7 on 2025-04-16 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0002_university_application_deadline_university_pace_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university',
            name='website',
        ),
        migrations.AddField(
            model_name='university',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='university_images/', verbose_name='Университет суреты'),
        ),
    ]
