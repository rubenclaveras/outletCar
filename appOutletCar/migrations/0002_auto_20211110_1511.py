# Generated by Django 3.2.8 on 2021-11-10 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appOutletCar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coche',
            name='categoria',
        ),
        migrations.AddField(
            model_name='coche',
            name='anyo',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
