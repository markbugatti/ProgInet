# Generated by Django 2.1.7 on 2019-06-08 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicationmodels', '0005_auto_20190608_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='example',
            name='ch',
            field=models.CharField(max_length=5, verbose_name="Ім'я"),
        ),
    ]
