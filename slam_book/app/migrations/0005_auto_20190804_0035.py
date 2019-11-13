# Generated by Django 2.2.3 on 2019-08-03 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_admin_login_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Login1',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Admin_Login',
        ),
    ]
