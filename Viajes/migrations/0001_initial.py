# Generated by Django 3.1.2 on 2020-11-15 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aeropuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=3, verbose_name='COD')),
                ('ciudad', models.CharField(max_length=50, verbose_name='Ciudad')),
            ],
        ),
    ]