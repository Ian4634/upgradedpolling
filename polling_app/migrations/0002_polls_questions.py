# Generated by Django 3.2.5 on 2021-08-03 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polling_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='polls',
            name='questions',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
