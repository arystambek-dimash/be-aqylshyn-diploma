# Generated by Django 5.1.7 on 2025-04-17 08:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general_english', '0005_alter_listeningquestion_audio_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptionAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_id', models.IntegerField()),
                ('correct_option_id', models.IntegerField()),
                ('module_score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option_attempts', to='general_english.modulescore')),
            ],
        ),
        migrations.CreateModel(
            name='WritingAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writing', models.TextField()),
                ('ai_response', models.TextField()),
                ('module_score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writing_attempts', to='general_english.modulescore')),
            ],
        ),
    ]
