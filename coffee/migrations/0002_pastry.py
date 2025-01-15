# Generated by Django 5.1.4 on 2025-01-15 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pastry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('image', models.CharField(max_length=2083)),
            ],
        ),
    ]
