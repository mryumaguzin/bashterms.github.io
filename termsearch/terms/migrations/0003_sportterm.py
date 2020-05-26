# Generated by Django 2.2.1 on 2020-05-20 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terms', '0002_auto_20200512_2115'),
    ]

    operations = [
        migrations.CreateModel(
            name='SportTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bash', models.CharField(max_length=255)),
                ('mean', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'sport_terms',
            },
        ),
    ]