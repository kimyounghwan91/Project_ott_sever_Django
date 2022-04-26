# Generated by Django 3.1.3 on 2022-04-01 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=4000, null=True)),
                ('opening_date', models.CharField(blank=True, max_length=1000, null=True)),
                ('just_rating', models.CharField(blank=True, max_length=1000, null=True)),
                ('imdb_rating', models.CharField(blank=True, max_length=1000, null=True)),
                ('runtime', models.CharField(blank=True, max_length=500, null=True)),
                ('synopsis', models.CharField(blank=True, max_length=4000, null=True)),
                ('director', models.CharField(blank=True, max_length=1000, null=True)),
                ('actors', models.CharField(blank=True, max_length=4000, null=True)),
                ('genre', models.CharField(blank=True, max_length=4000, null=True)),
                ('poster_link', models.CharField(blank=True, max_length=1000, null=True)),
                ('netflix', models.IntegerField(blank=True, null=True)),
                ('disneyplus', models.IntegerField(blank=True, null=True)),
                ('wavve', models.IntegerField(blank=True, null=True)),
                ('watcha', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movie',
                'managed': False,
            },
        ),
    ]
