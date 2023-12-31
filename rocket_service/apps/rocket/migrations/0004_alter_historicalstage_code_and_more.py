# Generated by Django 4.2.6 on 2023-10-31 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rocket', '0003_alter_stage_rocket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalstage',
            name='code',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='historicalstage',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stage',
            name='code',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stage',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='stage',
            unique_together={('rocket', 'name', 'code')},
        ),
    ]
