# Generated by Django 3.2.10 on 2021-12-19 16:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='имя кошки')),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entryTime', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='когда дали таблетку')),
                ('catId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.cat')),
            ],
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entryTime', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='когда покормлен')),
                ('size', models.IntegerField(default=0, verbose_name='размер порции')),
                ('catId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.cat')),
            ],
        ),
    ]