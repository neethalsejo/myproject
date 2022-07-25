# Generated by Django 3.2.13 on 2022-07-10 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0007_hospital_dimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='dimage',
            new_name='entimage',
        ),
        migrations.AddField(
            model_name='hospital',
            name='gynacimage',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='hospital',
            name='pediaimage',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='hospital',
            name='phyimage',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='hospital',
            name='uroimage',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
    ]