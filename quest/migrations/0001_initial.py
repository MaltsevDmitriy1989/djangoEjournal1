# Generated by Django 4.2.3 on 2023-08-22 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='T102Fak',
            fields=[
                ('fak_num', models.IntegerField(primary_key=True, serialize=False)),
                ('fak_namp', models.CharField(blank=True, max_length=255)),
                ('fak_nams', models.CharField(blank=True, max_length=60)),
                ('mesto', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'факультет',
                'verbose_name_plural': 'факультеты',
                'db_table': 't102_fak',
            },
        ),
        migrations.CreateModel(
            name='T121Quest',
            fields=[
                ('quest_num', models.AutoField(primary_key=True, serialize=False)),
                ('QuestID', models.IntegerField(blank=True, null=True)),
                ('baza_num', models.IntegerField(blank=True, null=True)),
                ('disc_num', models.IntegerField(blank=True, null=True)),
                ('quest_text', models.TextField(blank=True)),
                ('quest_text_etalon', models.TextField(blank=True)),
                ('quest_lev', models.IntegerField(blank=True, null=True)),
                ('quest_type', models.IntegerField(blank=True, null=True)),
                ('answer_kol', models.IntegerField(blank=True, null=True)),
                ('answer', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'вопрос',
                'verbose_name_plural': 'вопросы',
                'db_table': 't121_quest',
            },
        ),
        migrations.CreateModel(
            name='T122Answer',
            fields=[
                ('answer_num', models.IntegerField(primary_key=True, serialize=False)),
                ('quest_num', models.IntegerField(blank=True, null=True)),
                ('answer_type', models.IntegerField(blank=True, null=True)),
                ('ok', models.IntegerField(blank=True, null=True)),
                ('ans', models.IntegerField(blank=True, null=True)),
                ('answer_text', models.TextField(blank=True)),
                ('AnswerID', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'ответ',
                'verbose_name_plural': 'ответы',
                'db_table': 't122_answer',
            },
        ),
        migrations.CreateModel(
            name='T125Parol',
            fields=[
                ('parol_num', models.AutoField(primary_key=True, serialize=False)),
                ('plan_num', models.IntegerField()),
                ('fam', models.CharField(blank=True, max_length=40)),
                ('imya', models.CharField(blank=True, max_length=30)),
                ('otch', models.CharField(blank=True, max_length=30)),
                ('group_nam', models.CharField(blank=True, max_length=20)),
                ('pred_nam', models.CharField(blank=True, max_length=30)),
                ('baza_num', models.IntegerField()),
                ('stud_num', models.IntegerField()),
                ('password', models.CharField(max_length=36)),
                ('trying', models.IntegerField()),
            ],
            options={
                'verbose_name': 'пароль',
                'verbose_name_plural': 'пароли',
                'db_table': 't125_parol',
            },
        ),
        migrations.CreateModel(
            name='T125Plan',
            fields=[
                ('plan_num', models.IntegerField(primary_key=True, serialize=False)),
                ('baza_num', models.IntegerField(blank=True, null=True)),
                ('group_nam', models.CharField(max_length=20)),
                ('pred_nam', models.CharField(max_length=50)),
                ('group_num', models.IntegerField(blank=True, null=True)),
                ('fak_num', models.IntegerField(blank=True, null=True)),
                ('processed', models.IntegerField(blank=True, null=True)),
                ('executed', models.IntegerField(blank=True, null=True)),
                ('teacher_num', models.IntegerField(blank=True, null=True)),
                ('tester_num', models.IntegerField(blank=True, null=True)),
                ('test_date', models.DateField(blank=True, null=True)),
                ('test_time', models.TimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'план тестирования',
                'verbose_name_plural': 'планы тестования',
                'db_table': 't125_plan',
            },
        ),
        migrations.CreateModel(
            name='T125Session',
            fields=[
                ('session_num', models.AutoField(primary_key=True, serialize=False)),
                ('parol', models.CharField(blank=True, max_length=12)),
                ('plan_num', models.IntegerField(blank=True, null=True)),
                ('repeating', models.IntegerField(blank=True, null=True)),
                ('processed', models.IntegerField(blank=True, null=True)),
                ('trying', models.IntegerField(blank=True, null=True)),
                ('attempt', models.IntegerField(blank=True, null=True)),
                ('datetime_v', models.DateTimeField(blank=True, null=True)),
                ('ip_address', models.CharField(blank=True, max_length=15)),
                ('session_code', models.CharField(blank=True, max_length=36)),
            ],
            options={
                'verbose_name': 'сеанс',
                'verbose_name_plural': 'сеансы',
                'db_table': 't125_session',
            },
        ),
        migrations.CreateModel(
            name='T125Testing',
            fields=[
                ('testing_num', models.AutoField(primary_key=True, serialize=False)),
                ('parol', models.CharField(blank=True, max_length=12)),
                ('plan_num', models.IntegerField(blank=True, null=True)),
                ('repeating', models.IntegerField(blank=True, null=True)),
                ('processed', models.IntegerField(blank=True, null=True)),
                ('trying', models.IntegerField(blank=True, null=True)),
                ('attempt', models.IntegerField(blank=True, null=True)),
                ('datetime_v', models.DateTimeField(blank=True, null=True)),
                ('ip_address', models.CharField(blank=True, max_length=15)),
                ('session_code', models.CharField(blank=True, max_length=36)),
            ],
            options={
                'verbose_name': 'тестирование',
                'verbose_name_plural': 'тестирования',
                'db_table': 't125_testing',
            },
        ),
        migrations.CreateModel(
            name='T126Test',
            fields=[
                ('test_num', models.AutoField(primary_key=True, serialize=False)),
                ('plan_num', models.IntegerField(blank=True, null=True)),
                ('stud_num', models.IntegerField(blank=True, null=True)),
                ('baza_num', models.IntegerField(blank=True, null=True)),
                ('mark', models.FloatField(blank=True, null=True)),
                ('time', models.DateTimeField(blank=True, null=True)),
                ('ipaddr', models.CharField(blank=True, max_length=45)),
            ],
            options={
                'verbose_name': 'тест',
                'verbose_name_plural': 'тесты',
                'db_table': 't126_test',
            },
        ),
        migrations.CreateModel(
            name='T127ResTest',
            fields=[
                ('res_test_num', models.AutoField(primary_key=True, serialize=False)),
                ('test_num', models.IntegerField(blank=True, null=True)),
                ('quest_num', models.IntegerField(blank=True, null=True)),
                ('answer', models.CharField(blank=True, max_length=500)),
                ('quest_typ', models.IntegerField(blank=True, null=True)),
                ('ball', models.FloatField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'результаты тестирования',
                'verbose_name_plural': 'результаты тестирования',
                'db_table': 't127_res_test',
            },
        ),
        migrations.CreateModel(
            name='T190Admin',
            fields=[
                ('admin_num', models.AutoField(primary_key=True, serialize=False)),
                ('fam', models.CharField(max_length=40)),
                ('imya', models.CharField(max_length=30)),
                ('otch', models.CharField(max_length=30)),
                ('pass_md5', models.CharField(max_length=40)),
                ('priv_num', models.IntegerField(blank=True, null=True)),
                ('priv_nam', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'администратор',
                'verbose_name_plural': 'администраторы',
                'db_table': 't190_admin',
            },
        ),
        migrations.CreateModel(
            name='T190Prepod',
            fields=[
                ('prepod_num', models.AutoField(primary_key=True, serialize=False)),
                ('fam', models.CharField(max_length=40)),
                ('imya', models.CharField(max_length=30)),
                ('otch', models.CharField(max_length=30)),
                ('pass_md5', models.CharField(max_length=40)),
                ('priv_num', models.IntegerField(blank=True, null=True)),
                ('priv_nam', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'преподаватель',
                'verbose_name_plural': 'преподаватели',
                'db_table': 't190_prepod',
            },
        ),
    ]
