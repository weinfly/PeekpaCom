# Generated by Django 2.1.15 on 2020-05-29 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basefunction', '0007_auto_20200529_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='featurepost',
            name='status',
            field=models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除'), (2, '草稿')], default=2),
        ),
    ]
