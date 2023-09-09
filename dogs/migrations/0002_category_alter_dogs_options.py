# Generated by Django 4.2.5 on 2023-09-06 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Порода')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
        ),
        migrations.AlterModelOptions(
            name='dogs',
            options={'verbose_name': 'собака', 'verbose_name_plural': 'собаки'},
        ),
    ]