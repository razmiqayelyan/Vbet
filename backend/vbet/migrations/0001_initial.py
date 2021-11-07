# Generated by Django 3.2 on 2021-11-06 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vbet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('company', models.CharField(max_length=15)),
                ('position', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='media/')),
                ('phone', models.CharField(max_length=16)),
            ],
        ),
    ]
