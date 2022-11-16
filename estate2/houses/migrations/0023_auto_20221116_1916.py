# Generated by Django 3.2.14 on 2022-11-16 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('houses', '0022_footer_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='in_advance_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='house',
            name='number_of_installments',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='house',
            name='time_of_delivery',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_paragraph', models.CharField(default='We Do Great Design For Creative Folks', max_length=100)),
                ('img1', models.ImageField(default='some img1', upload_to='images')),
                ('name1', models.CharField(default='red winners', max_length=50)),
                ('img2', models.ImageField(default='some img2', upload_to='images')),
                ('since_when', models.CharField(default='Since 2017', max_length=50)),
                ('name2', models.CharField(max_length=50)),
                ('description1', models.TextField(default='Enter description 2 here')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]