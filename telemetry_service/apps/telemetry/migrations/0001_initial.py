# Generated by Django 4.2.6 on 2023-10-31 03:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Telemetry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rocket_code', models.CharField(max_length=255)),
                ('rocket_name', models.CharField(max_length=255)),
                ('stage_code', models.CharField(max_length=255)),
                ('stage_name', models.CharField(max_length=255)),
                ('engine_code', models.CharField(max_length=255)),
                ('engine_name', models.CharField(max_length=255)),
                ('speed', models.FloatField()),
                ('altitude', models.FloatField()),
                ('thrust', models.FloatField()),
                ('isp', models.FloatField()),
                ('temperature', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalTelemetry',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('rocket_code', models.CharField(max_length=255)),
                ('rocket_name', models.CharField(max_length=255)),
                ('stage_code', models.CharField(max_length=255)),
                ('stage_name', models.CharField(max_length=255)),
                ('engine_code', models.CharField(max_length=255)),
                ('engine_name', models.CharField(max_length=255)),
                ('speed', models.FloatField()),
                ('altitude', models.FloatField()),
                ('thrust', models.FloatField()),
                ('isp', models.FloatField()),
                ('temperature', models.FloatField()),
                ('timestamp', models.DateTimeField(blank=True, editable=False)),
                ('created_at', models.DateTimeField(blank=True, editable=False)),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical telemetry',
                'verbose_name_plural': 'historical telemetrys',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
