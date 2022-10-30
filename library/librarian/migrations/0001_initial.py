# Generated by Django 4.1.2 on 2022-10-30 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('author', models.CharField(default='', max_length=255)),
                ('publisher', models.CharField(default='', max_length=255)),
                ('year', models.CharField(default='', max_length=4)),
                ('edition', models.CharField(default='', max_length=255)),
                ('availability', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('membernum', models.CharField(max_length=8)),
            ],
        ),
    ]
