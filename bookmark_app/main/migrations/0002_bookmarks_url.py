# Generated by Django 4.1 on 2022-08-22 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmarks',
            name='url',
            field=models.URLField(default=None),
        ),
    ]