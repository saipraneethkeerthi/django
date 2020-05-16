# Generated by Django 3.0.6 on 2020-05-14 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_projects_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myeducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=20)),
                ('study', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=500)),
                ('branch', models.CharField(max_length=100)),
                ('branchIs', models.BooleanField(default=False)),
                ('cgpa', models.FloatField(max_length=10)),
            ],
        ),
    ]
