# Generated by Django 3.2.11 on 2022-01-18 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания записи')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='Имя организации')),
                ('logo', models.FileField(max_length=64, null=True, upload_to='', verbose_name='Логотип организации')),
                ('url', models.URLField(max_length=64, null=True, verbose_name='Сайт компании')),
                ('city', models.CharField(db_index=True, max_length=64, null=True, verbose_name='Город')),
                ('address', models.CharField(max_length=64, null=True, verbose_name='Адрес организации')),
                ('description', models.TextField(max_length=5000, null=True, verbose_name='Описание организации')),
                ('is_active', models.BooleanField(db_index=True, default=False, verbose_name='Активность')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Организации',
            },
        ),
    ]
