# Generated by Django 2.1.5 on 2019-01-16 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
