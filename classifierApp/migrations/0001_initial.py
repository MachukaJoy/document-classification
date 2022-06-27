# Generated by Django 3.2.13 on 2022-06-27 08:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagepath', models.TimeField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('predicted', models.TextField()),
                ('confidence', models.IntegerField(blank=True, default=0, null=True)),
                ('saved', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-saved',),
            },
        ),
    ]
