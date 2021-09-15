# Generated by Django 3.1.3 on 2021-09-15 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('trailer', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('rating', models.IntegerField(null=True)),
                ('show', models.BooleanField(default=True)),
            ],
        ),
    ]