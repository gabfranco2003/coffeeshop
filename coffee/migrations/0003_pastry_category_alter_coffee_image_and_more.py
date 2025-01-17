# Generated by Django 5.1.4 on 2025-01-15 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0002_pastry'),
    ]

    operations = [
        migrations.AddField(
            model_name='pastry',
            name='category',
            field=models.CharField(default='Uncategorized', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coffee',
            name='image',
            field=models.ImageField(upload_to='coffee/'),
        ),
        migrations.AlterField(
            model_name='pastry',
            name='image',
            field=models.ImageField(upload_to='pastries/'),
        ),
        migrations.AlterField(
            model_name='pastry',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pastry',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
