# Generated by Django 4.2.2 on 2023-06-21 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_description_project_git_project_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tech',
            field=models.ManyToManyField(blank=True, to='portfolio.tech'),
        ),
    ]
