# Generated by Django 2.2.3 on 2019-08-06 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_user_login1'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_login1',
            name='phone_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
