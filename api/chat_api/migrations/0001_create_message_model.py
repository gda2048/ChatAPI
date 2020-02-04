# Generated by Django 2.2.5 on 2020-02-04 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(help_text='Содержание письма может быть максимум в 4095 символов', max_length=4095, verbose_name='Содержание сообщения')),
                ('subject', models.CharField(help_text='Тема сообщения может быть максимум в 255 символов', max_length=255, verbose_name='Тема сообщения')),
                ('is_read', models.BooleanField(default=False, verbose_name='Прочитано ли?')),
                ('creation_date', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('receiver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='got_messages', to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent_messages', to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
                'db_table': 'messages',
                'ordering': ['-creation_date'],
            },
        ),
    ]
