# Generated by Django 3.2.13 on 2022-05-30 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_first_migration'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created']},
        ),
    ]
