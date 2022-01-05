# Generated by Django 3.2.5 on 2021-11-30 23:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tracker.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=32, unique=True)),
                ('desc', models.CharField(default='please enter a description', max_length=512)),
                ('link', models.URLField(max_length=1024)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component', models.CharField(max_length=32, unique=True)),
                ('desc', models.CharField(max_length=512)),
                ('img', models.URLField(blank=True, max_length=1024)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=32, unique=True)),
                ('desc', models.CharField(max_length=512)),
                ('status', models.CharField(choices=[('Live', 'Live'), ('Release Candidate', 'Review'), ('Beta', 'Beta'), ('Alpha', 'Alpha'), ('Pre Alpha', 'Prealpha'), ('Concept', 'Concept')], default='Concept', max_length=24)),
                ('img', models.URLField(blank=True, max_length=1024)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UseCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('use_case', models.CharField(max_length=32, unique=True)),
                ('desc', models.CharField(max_length=512)),
                ('doc', models.URLField(blank=True, max_length=1024)),
                ('status', models.CharField(choices=[('Live', 'Live'), ('Not Supported', 'Na'), ('Queued', 'Queued'), ('Review', 'Review')], max_length=24)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_need_to', models.CharField(max_length=256)),
                ('then', models.CharField(blank=True, max_length=256)),
                ('operator', models.CharField(blank=True, choices=[('AND', 'And'), ('OR', 'Or')], max_length=3)),
                ('so_that', models.CharField(max_length=128)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('usecase', models.ForeignKey(default=models.SET(tracker.models.get_usecase_id), on_delete=django.db.models.deletion.CASCADE, to='tracker.usecase')),
            ],
        ),
        migrations.CreateModel(
            name='UseCase_UserStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usecase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.usecase')),
                ('userstory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.userstory')),
            ],
        ),
        migrations.CreateModel(
            name='Product_UseCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Live', 'Live'), ('Not Supported', 'Na'), ('Queued', 'Queued'), ('Review', 'Review')], default='Queued', max_length=24, verbose_name='Status')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.product')),
                ('usecase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.usecase')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.component')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.product')),
            ],
        ),
        migrations.CreateModel(
            name='Client_UseCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Live', 'Live'), ('Not Supported', 'Na'), ('Queued', 'Queued'), ('Review', 'Review')], default='Review', max_length=24, verbose_name='Status')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.client')),
                ('usecase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.usecase')),
            ],
        ),
        migrations.CreateModel(
            name='Client_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Live', 'Live'), ('In Trial', 'Trial'), ('Opportunity', 'Opp'), ('Warm Lead', 'Warm'), ('Implementation', 'Imp'), ('Opportunity Under Review', 'Review'), ('Did not Purchase', 'Closed')], default='OPP', max_length=24)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.client')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.product')),
            ],
        ),
    ]