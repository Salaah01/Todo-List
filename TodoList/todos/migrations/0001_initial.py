# Generated by Django 2.2 on 2019-04-21 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=100)),
                ('date_set', models.DateTimeField()),
                ('due_date', models.DateTimeField()),
            ],
        ),
    ]