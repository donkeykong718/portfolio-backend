# Generated by Django 4.2.2 on 2023-06-21 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='git',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(default=''),
        ),
    ]
