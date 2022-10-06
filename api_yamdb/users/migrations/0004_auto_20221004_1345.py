# Generated by Django 2.2.28 on 2022-10-04 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20221004_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.TextField(blank=True, choices=[('user', 'User'), ('moderator', 'Moderator'), ('admin', 'Admin')], default='user'),
        ),
    ]