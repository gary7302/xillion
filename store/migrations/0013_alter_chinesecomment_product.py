# Generated by Django 4.1.7 on 2023-07-04 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_rename_orde_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chinesecomment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chinesecomment', to='store.chineseproduct'),
        ),
    ]
