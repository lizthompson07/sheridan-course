# Generated by Django 3.2.13 on 2022-06-02 01:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20220601_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='blog_posts', to='auth.user'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='The date & time this article was published', unique_for_date='published'),
        ),
    ]
