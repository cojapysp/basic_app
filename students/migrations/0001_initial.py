# Generated by Django 3.2.7 on 2021-09-24 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_data',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('roll_no', models.IntegerField(max_length=100)),
                ('grade', models.FloatField(max_length=100)),
                ('result', models.CharField(max_length=100)),
            ],
        ),
    ]
