# Generated by Django 3.2.13 on 2022-06-30 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0002_alter_patient_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]