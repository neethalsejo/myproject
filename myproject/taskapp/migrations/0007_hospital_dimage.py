# Generated by Django 3.2.13 on 2022-07-10 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0006_alter_patient_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='dimage',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
    ]