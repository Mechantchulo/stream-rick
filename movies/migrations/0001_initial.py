# Generated by Django 5.0.7 on 2024-08-22 16:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre')),
            ],
        ),
    ]
