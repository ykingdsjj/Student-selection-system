# Generated by Django 2.0.2 on 2018-03-04 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20180304_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherapplycourse',
            name='status',
            field=models.CharField(choices=[('审核中', '审核中'), ('批准', '批准'), ('不同意', '不同意')], default='审核中', max_length=3, verbose_name='状态'),
        ),
    ]