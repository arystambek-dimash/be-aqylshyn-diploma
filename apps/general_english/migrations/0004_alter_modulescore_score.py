# Generated by Django 5.1.7 on 2025-04-10 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_english', '0003_readingquestion_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulescore',
            name='score',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
