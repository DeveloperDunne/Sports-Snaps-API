# Generated by Django 5.0.7 on 2024-08-08 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='subject',
        ),
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default='test message', max_length=500),
            preserve_default=False,
        ),
    ]
