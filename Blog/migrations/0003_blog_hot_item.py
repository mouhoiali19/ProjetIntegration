# Generated by Django 5.1.6 on 2025-02-05 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_categories_blogs_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='hot_item',
            field=models.CharField(default='crypto', max_length=100),
        ),
    ]
