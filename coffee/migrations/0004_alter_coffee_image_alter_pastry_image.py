# Generated by Django 5.1.4 on 2025-01-15 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0003_pastry_category_alter_coffee_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='image',
            field=models.URLField(blank=True, max_length=2080, null=True),
        ),
        migrations.AlterField(
            model_name='pastry',
            name='image',
            field=models.URLField(blank=True, max_length=2080, null=True),
        ),
    ]
