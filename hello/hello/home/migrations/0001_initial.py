# Generated by Django 4.0.4 on 2022-05-24 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=120)),
                ('Email', models.CharField(max_length=30)),
                ('Address', models.CharField(max_length=20)),
                ('Number', models.CharField(max_length=12)),
                ('City', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('code', models.CharField(max_length=6)),
            ],
        ),
    ]