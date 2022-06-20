# Generated by Django 3.2.13 on 2022-06-02 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.DateTimeField(blank=True, help_text='The date & time this article was published', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='The date & time this article was published', null=True, unique_for_date='published'),
        ),
    ]