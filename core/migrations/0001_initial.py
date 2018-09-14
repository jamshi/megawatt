# Generated by Django 2.1.1 on 2018-09-14 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Site Name')),
            ],
        ),
        migrations.CreateModel(
            name='SiteDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('a_value', models.FloatField()),
                ('b_value', models.FloatField()),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Site')),
            ],
        ),
    ]
