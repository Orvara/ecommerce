# Generated by Django 2.2.8 on 2020-05-22 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200522_0412'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
