# Generated by Django 5.1.1 on 2024-10-16 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact',
            field=models.IntegerField(max_length=300, verbose_name='Contact No'),
        ),
    ]