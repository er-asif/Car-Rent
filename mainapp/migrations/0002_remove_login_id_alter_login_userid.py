# Generated by Django 5.0.4 on 2024-04-30 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='id',
        ),
        migrations.AlterField(
            model_name='login',
            name='userid',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
