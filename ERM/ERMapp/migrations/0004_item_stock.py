# Generated by Django 5.1.6 on 2025-02-24 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ERMapp', '0003_alter_item_description_alter_item_itemname'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='stock',
            field=models.IntegerField(null=True),
        ),
    ]
