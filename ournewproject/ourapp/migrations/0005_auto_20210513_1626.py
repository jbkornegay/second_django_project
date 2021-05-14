# Generated by Django 3.2.2 on 2021-05-13 20:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ourapp', '0004_alter_student_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('passing_grade', models.BooleanField(default=True)),
            ],
        ),
        migrations.RenameField(
            model_name='school',
            old_name='name',
            new_name='school_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='age',
            new_name='graduation_year',
        ),
        migrations.RemoveField(
            model_name='student',
            name='date_of_resumption',
        ),
        migrations.RemoveField(
            model_name='student',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name',
        ),
        migrations.AddField(
            model_name='student',
            name='full_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=50)),
                ('Faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ourapp.faculty')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='Certificate_Type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ourapp.certificate_type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='Department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ourapp.department'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='Grade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ourapp.grade'),
            preserve_default=False,
        ),
    ]
