# Generated by Django 3.1.14 on 2022-01-08 22:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq_number', models.CharField(max_length=10)),
                ('equipment_name', models.CharField(max_length=50)),
                ('serial_number', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True, max_length=250, unique=True)),
                ('entry', models.DateTimeField(default=django.utils.timezone.now)),
                ('tag_number', models.CharField(blank=True, max_length=30)),
                ('status', models.CharField(choices=[('inactive', 'Inactive'), ('active', 'Active'), ('faulty', 'Faulty')], default='inactive', max_length=30)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-entry',),
            },
        ),
    ]
