# Generated by Django 3.0.8 on 2020-08-30 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200830_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurementresults',
            name='data_id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='データ番号'),
        ),
    ]