# Generated by Django 2.1.7 on 2019-06-07 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ch', models.CharField(max_length=5)),
                ('txt', models.TextField(max_length=20)),
                ('date', models.DateField()),
                ('dateTime', models.DateTimeField()),
                ('dc', models.DecimalField(decimal_places=2, max_digits=8)),
                ('em', models.EmailField(max_length=254)),
            ],
        ),
    ]
