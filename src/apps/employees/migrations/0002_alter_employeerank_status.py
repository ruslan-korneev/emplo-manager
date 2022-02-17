# Generated by Django 4.0.2 on 2022-02-17 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeerank',
            name='status',
            field=models.CharField(choices=[('the-best', 'Лучший'), ('trainee', 'Стажер'), ('employee', 'Сотрудник')], max_length=255, verbose_name='Статус'),
        ),
    ]
