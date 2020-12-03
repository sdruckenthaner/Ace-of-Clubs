# Generated by Django 3.1.4 on 2020-12-03 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aceofclubs', '0003_auto_20201203_1336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='description',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='group',
        ),
        migrations.AlterField(
            model_name='event',
            name='group',
            field=models.ManyToManyField(blank=True, to='aceofclubs.Group'),
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_leader', models.BooleanField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aceofclubs.group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aceofclubs.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aceofclubs.event')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aceofclubs.state')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aceofclubs.user')),
            ],
        ),
    ]
