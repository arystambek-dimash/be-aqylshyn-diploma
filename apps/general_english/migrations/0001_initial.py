# Generated by Django 5.1.7 on 2025-04-03 09:13

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0002_alter_course_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ListeningQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio_question', models.FileField(upload_to='', verbose_name='Аудио сұрақ')),
                ('context', models.CharField(verbose_name='Аудио сұрақ тексті')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Модуль атауы')),
                ('is_completed', models.BooleanField(default=False, verbose_name='Модуль аяқталыдма?')),
                ('improvement', models.TextField(verbose_name='Қолданушыға бағытталған күшейтулер')),
                ('has_writing', models.BooleanField(default=True)),
                ('has_reading', models.BooleanField(default=True)),
                ('has_listening', models.BooleanField(default=True)),
                ('has_speaking', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ListeningOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.TextField(help_text='Бұл жауап нұсқасының мәтіні', verbose_name='Нұсқа мәтіні')),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='general_english.listeningquestion', verbose_name='Сұрақ')),
            ],
        ),
        migrations.AddField(
            model_name='listeningquestion',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listening_questions', to='general_english.module'),
        ),
        migrations.CreateModel(
            name='ModuleScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(choices=[('READING', 'Reading'), ('WRITING', 'Writing'), ('LISTENING', 'LISTENING'), ('SPEAKING', 'Speaking')], max_length=10)),
                ('score', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general_english.module')),
            ],
        ),
        migrations.CreateModel(
            name='ReadingQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.TextField(help_text='Бұл сұрақ қатысты мәтін үзіндісі', verbose_name='Оқу мәтіні')),
                ('image', models.URLField(blank=True, null=True, verbose_name='Сурет сілтемесі')),
                ('source', models.TextField(blank=True, null=True, verbose_name='Дереккөз')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='readings', to='general_english.module', verbose_name='Қай модульге тиесілі')),
            ],
        ),
        migrations.CreateModel(
            name='ReadingOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.TextField(help_text='Бұл жауап нұсқасының мәтіні', verbose_name='Нұсқа мәтіні')),
                ('is_correct', models.BooleanField(default=False, help_text='Бұл нұсқа дұрыс жауап болып табылады ма', verbose_name='Дұрыс па')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='general_english.readingquestion', verbose_name='Сұрақ')),
            ],
        ),
        migrations.CreateModel(
            name='Speaking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.CharField(max_length=255)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speakings', to='general_english.module', verbose_name='Қай модульге тиесілі')),
            ],
        ),
        migrations.CreateModel(
            name='TrialQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, verbose_name='Сұрақ мәтіні')),
                ('question_type', models.CharField(choices=[('SINGLE_CHOICE', 'Single choice'), ('TEXT_ANSWER', 'Text answer')], default='SINGLE_CHOICE', verbose_name='Сұрақ типі')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trial_questions', to='courses.course', verbose_name='Қай курсқа тиесілі')),
            ],
            options={
                'verbose_name': 'Сынама сұрақ',
                'verbose_name_plural': 'Сынама сұрақтар',
            },
        ),
        migrations.CreateModel(
            name='TrialOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=200, verbose_name='Опция')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Бұл дұрыс опцияма?')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trial_options', to='general_english.trialquestion', verbose_name='Қай сұраққа тиесілі')),
            ],
            options={
                'verbose_name': 'Сынама сұрақ опциясы',
                'verbose_name_plural': 'Сынама сұрақ опциялары',
            },
        ),
        migrations.CreateModel(
            name='UserProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Қолданушының жинаған ұпай саны')),
                ('level', models.CharField(null=True, verbose_name='Қолданушы уровеньі')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_course', to='courses.course', verbose_name='Қай курсқа тіркелген')),
                ('last_module', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='general_english.module', verbose_name='Тоқтаған модуль')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_progresses', to=settings.AUTH_USER_MODEL, verbose_name='Тіркелген қолданушы')),
            ],
            options={
                'unique_together': {('course', 'user')},
            },
        ),
        migrations.AddField(
            model_name='module',
            name='user_course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_modules', to='general_english.userprogress', verbose_name='Қолданушы курсы'),
        ),
        migrations.CreateModel(
            name='Writing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(help_text='Бұл сұрақ қатысты мәтін үзіндісі', verbose_name='Оқу мазмүны')),
                ('requirements', models.TextField(help_text='Бұл түсініктеме қолданшыны тексергенде қаралатын анықтама секілді', verbose_name='Тема түсініктемесі')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writing', to='general_english.module', verbose_name='Қай модульге тиесілі')),
            ],
        ),
    ]
