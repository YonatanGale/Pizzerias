# Generated by Django 4.1.7 on 2023-05-16 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzeria',
            name='state',
            field=models.CharField(blank=True, default=1, max_length=2),
            preserve_default=False,
        ),
    ]
