# Generated by Django 2.0.5 on 2019-07-07 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_customers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customers',
        ),
    ]