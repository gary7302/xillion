# Generated by Django 4.1.7 on 2023-07-03 11:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0011_orde_alter_orderitems_order_delete_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orde',
            new_name='Order',
        ),
    ]
