# Generated by Django 3.2.13 on 2022-07-10 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0009_auto_20220710_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='entimage',
            field=models.ImageField(upload_to='img'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='gynacimage',
            field=models.ImageField(upload_to='img'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='pediaimage',
            field=models.ImageField(upload_to='img'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='phyimage',
            field=models.ImageField(upload_to='img'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='uroimage',
            field=models.ImageField(upload_to='img'),
        ),
    ]