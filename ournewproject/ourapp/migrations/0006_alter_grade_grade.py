# Generated by Django 3.2.2 on 2021-05-13 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourapp', '0005_auto_20210513_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.CharField(max_length=10),
        ),
    ]
