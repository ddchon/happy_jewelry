# Generated by Django 2.2.2 on 2019-06-14 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20190613_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='add_to_cart',
            field=models.BooleanField(default=False),
        ),
    ]