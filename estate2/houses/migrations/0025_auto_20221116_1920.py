# Generated by Django 3.2.14 on 2022-11-16 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0024_remove_about_name2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='about',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]