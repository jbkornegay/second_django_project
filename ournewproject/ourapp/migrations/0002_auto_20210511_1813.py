# Generated by Django 3.2.2 on 2021-05-11 22:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ourapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='address',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='name',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='school',
            name='postal_code',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='School',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ourapp.school'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='date_of_resumption',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
