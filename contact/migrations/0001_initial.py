# Generated by Django 5.0.6 on 2024-07-10 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact_master',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('mobile', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
            ],
        ),
    ]
