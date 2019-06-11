# Generated by Django 2.1.7 on 2019-06-10 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('birth', models.DateField()),
                ('company', models.CharField(choices=[('e', 'Epam'), ('gl', 'Global Logic'), ('m', 'Microsoft'), ('gg', 'Google'), ('a', 'Amazon')], max_length=150)),
                ('position', models.CharField(choices=[('p', 'Programmer'), ('d', 'CEO'), ('m', 'Manager')], max_length=15)),
                ('language', models.CharField(choices=[('e', 'English'), ('f', 'Franch'), ('g', 'German'), ('u', 'Ukrainian'), ('r', 'Russion')], default='e', max_length=10)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]