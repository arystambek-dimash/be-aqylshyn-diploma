# Generated by Django 5.1.7 on 2025-04-17 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_english', '0006_optionattempt_writingattempt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='optionattempt',
            name='correct_option_id',
        ),
        migrations.AddField(
            model_name='optionattempt',
            name='question_id',
            field=models.IntegerField(null=True),
        ),
    ]
