# Generated by Django 3.2.5 on 2021-08-09 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polling_app', '0003_auto_20210809_1843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='polls',
            old_name='question1',
            new_name='questions',
        ),
        migrations.RemoveField(
            model_name='polls',
            name='questNumber',
        ),
        migrations.RemoveField(
            model_name='polls',
            name='question2',
        ),
        migrations.RemoveField(
            model_name='polls',
            name='question3',
        ),
        migrations.RemoveField(
            model_name='polls',
            name='question4',
        ),
        migrations.RemoveField(
            model_name='polls',
            name='question5',
        ),
        migrations.RemoveField(
            model_name='polls',
            name='question6',
        ),
        migrations.RemoveField(
            model_name='polls',
            name='question7',
        ),
        migrations.RemoveField(
            model_name='polls',
            name='question8',
        ),
    ]