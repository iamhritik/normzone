# Generated by Django 3.2.4 on 2021-06-19 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('normzone', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date',
            new_name='date_posted',
        ),
    ]
