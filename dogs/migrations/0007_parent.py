# Generated by Django 4.2.5 on 2023-09-25 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0006_alter_dog_birth_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Кличка')),
                ('birth_day', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogs.category', verbose_name='Порода')),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogs.dog', verbose_name='Собака')),
            ],
            options={
                'verbose_name': 'Предок',
                'verbose_name_plural': 'Предки',
            },
        ),
    ]
