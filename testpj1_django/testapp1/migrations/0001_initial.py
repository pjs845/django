# Generated by Django 4.0.6 on 2022-07-27 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('addr', models.TextField()),
                ('rdate', models.DateTimeField()),
            ],
        ),
    ]
