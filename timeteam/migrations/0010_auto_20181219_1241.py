# Generated by Django 2.1.4 on 2018-12-19 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeteam', '0009_auto_20181219_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultaat',
            name='totaal',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]