# Generated by Django 2.2.3 on 2019-07-19 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]