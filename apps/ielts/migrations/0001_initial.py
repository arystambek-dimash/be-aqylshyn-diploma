# Generated by Django 5.1.7 on 2025-04-03 09:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0002_alter_course_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='IeltsListening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField()),
                ('audio_file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='IeltsReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Мәтіннің атауы')),
                ('content', models.TextField(verbose_name='Мәтін')),
            ],
            options={
                'verbose_name': 'Оқу мәтіні',
                'verbose_name_plural': 'Оқу мәтіндері',
            },
        ),
        migrations.CreateModel(
            name='IeltsListeningQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question_content', models.TextField(verbose_name='Question Text')),
                ('question_type', models.CharField(choices=[('FILL', 'Fill in the Blank'), ('OPTIONS', 'Multiple Choice Options')], default='OPTIONS', max_length=32, verbose_name='Question Type')),
                ('listening', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='ielts.ieltslistening')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IeltsListeningOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=255, verbose_name='Жауап нұсқасы')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Дұрыс жауап па?')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='ielts.ieltslisteningquestion', verbose_name='Сұрақ')),
            ],
        ),
        migrations.CreateModel(
            name='IeltsListeningFillBlank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.JSONField(help_text='Жауаптар ретімен берілген массив түрінде болады', verbose_name='Дұрыс жауаптар тізімі')),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fill_blank', to='ielts.ieltslisteningquestion', verbose_name='Сұрақ')),
            ],
        ),
        migrations.CreateModel(
            name='IeltsModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cover', models.ImageField(upload_to='ielts/modules/', verbose_name='Модульдің суреті')),
                ('title', models.CharField(max_length=255, verbose_name='Модульдің атауы')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'IELTS модулі',
                'verbose_name_plural': 'IELTS модульдері',
            },
        ),
        migrations.CreateModel(
            name='IeltsReadingQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question_content', models.TextField(verbose_name='Question Text')),
                ('question_type', models.CharField(choices=[('FILL', 'Fill in the Blank'), ('SELECT_INSERT_ANSWER', 'Select and place in correct order'), ('OPTIONS', 'Multiple Choice Options')], default='OPTIONS', max_length=32, verbose_name='Question Type')),
                ('reading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='ielts.ieltsreading', verbose_name='Оқу мәтіні')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IeltsReadingOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=255, verbose_name='Жауап нұсқасы')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Дұрыс жауап па?')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='ielts.ieltsreadingquestion', verbose_name='Сұрақ')),
            ],
        ),
        migrations.CreateModel(
            name='IeltsReadingFillBlank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.JSONField(help_text='Жауаптар ретімен берілген массив түрінде болады', verbose_name='Дұрыс жауаптар тізімі')),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fill_blank', to='ielts.ieltsreadingquestion', verbose_name='Сұрақ')),
            ],
        ),
        migrations.CreateModel(
            name='IeltsReadingSelectInsert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_answer', models.TextField(help_text="Толық дұрыс сөйлем, мысалы: 'Сәлем Димаш, Сәлем Джейк'", verbose_name='Дұрыс сөйлем')),
                ('options', models.JSONField(help_text="Қолданушы таңдауы керек сөздер тізімі, мысалы: ['Димаш', 'Джейк']", verbose_name='Қолжетімді сөздер/сөз тіркестері')),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='select_insert_data', to='ielts.ieltsreadingquestion', verbose_name='Сұрақ')),
            ],
        ),
        migrations.CreateModel(
            name='IeltsSubModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Оқу секциясының атауы')),
                ('difficulty', models.CharField(choices=[('EASY', 'Easy'), ('MEDIUM', 'Medium'), ('HARD', 'Hard')], default='EASY', max_length=255, verbose_name='Қиындық дәрежесі')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_modules', to='ielts.ieltsmodule', verbose_name='IELTS модулі')),
            ],
            options={
                'verbose_name': 'Оқу тапсырмасы',
                'verbose_name_plural': 'Оқу тапсырмалары',
            },
        ),
        migrations.CreateModel(
            name='IeltsTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sub_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='ielts.ieltssubmodule')),
            ],
        ),
        migrations.AddField(
            model_name='ieltsreading',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='readings', to='ielts.ieltstest'),
        ),
        migrations.AddField(
            model_name='ieltslistening',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='listenings', to='ielts.ieltstest'),
        ),
        migrations.CreateModel(
            name='IeltsWriting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Тапсырма атауы')),
                ('description', models.TextField(verbose_name='Сипаттама')),
                ('context', models.TextField(verbose_name='Берілгені')),
                ('test', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='writings', to='ielts.ieltstest')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WritingImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ielts_writing/', verbose_name='Сурет')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='ielts.ieltswriting', verbose_name='Сурет')),
            ],
        ),
    ]
