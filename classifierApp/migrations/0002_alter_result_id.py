# Generated by Django 3.2.13 on 2022-06-27 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifierApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
