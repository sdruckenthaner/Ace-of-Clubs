# Generated by Django 3.1.4 on 2020-12-03 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aceofclubs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField()),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('pwhash', models.TextField()),
                ('active', models.BooleanField()),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aceofclubs.group')),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aceofclubs.permission')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('active', models.BooleanField()),
                ('ev_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aceofclubs.eventtype')),
                ('group', models.ManyToManyField(to='aceofclubs.Group')),
            ],
        ),
    ]
