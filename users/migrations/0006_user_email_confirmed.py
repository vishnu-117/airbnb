# Generated by Django 3.1a1 on 2020-05-25 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200520_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]