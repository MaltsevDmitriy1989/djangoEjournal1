# Generated by Django 4.2.3 on 2023-08-21 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationProgramm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studyduration', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256)),
                ('modeofstudy', models.CharField(max_length=256)),
                ('degree', models.CharField(max_length=256)),
                ('fieldofstudy', models.CharField(max_length=256)),
                ('image', models.ImageField(upload_to='products_images')),
            ],
            options={
                'verbose_name': 'Образовательная программа',
                'verbose_name_plural': 'Образовательные программы',
            },
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('level', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='sport_images')),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mediacontent.sports')),
            ],
        ),
    ]
