# Generated by Django 3.2.13 on 2022-07-10 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0008_auto_20220710_0420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(max_length=250),
        ),
    ]
