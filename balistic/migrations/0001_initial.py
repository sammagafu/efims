# Generated by Django 3.0.4 on 2020-08-20 06:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ballistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ourref', models.CharField(max_length=100, unique=True, verbose_name='Our REF')),
                ('yourref', models.CharField(max_length=100, unique=True, verbose_name='Your REF')),
                ('station', models.CharField(help_text='Enter Police Station', max_length=160, verbose_name='Police Station')),
                ('article', models.TextField(verbose_name='Article or Exhibits Received')),
                ('examination', models.TextField(verbose_name='Type of Examination')),
                ('addition', models.TextField(verbose_name='Addition Information')),
                ('received_date', models.DateTimeField(auto_now=True, verbose_name='Date Received')),
                ('deliver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deliver', to='pages.Client', verbose_name='delivering officer')),
                ('receicer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL, verbose_name='receiving officer')),
            ],
            options={
                'verbose_name': 'Ballistic',
                'verbose_name_plural': 'Ballistics',
            },
        ),
    ]