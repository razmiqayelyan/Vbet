# Generated by Django 3.2 on 2021-11-06 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vbet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vbet',
            name='company',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='vbet',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='vbet',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='vbet',
            name='phone',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='vbet',
            name='position',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
