# Generated by Django 2.1.3 on 2021-07-12 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=67)),
                ('phone', models.CharField(max_length=20)),
                ('register_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
