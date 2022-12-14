# Generated by Django 3.2.14 on 2022-10-13 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0007_house_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='location',
            field=models.CharField(blank=True, choices=[('Ain Shokana', 'Ain Shokana'), ('Ain Sokhna', 'Ain Sokhna'), ('Alexandria', 'Alexandria'), ('East Cairo', 'East Cairo'), ('Mostakbal City', 'Mostakbal City'), ('New Cairo', 'New Cairo'), ('New Capital', 'New Capital'), ('North Coast', 'North Coast'), ('Sheik Zayed', 'Sheik Zayed'), ('West Cairo', 'West Cairo'), ('6th of October', '6th of October'), ('New Zayed', 'New Zayed')], max_length=50, null=True),
        ),
    ]
