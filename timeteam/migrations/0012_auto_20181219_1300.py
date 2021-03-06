# Generated by Django 2.1.4 on 2018-12-19 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timeteam', '0011_auto_20181219_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wedstrijdbaan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=200)),
                ('locatie', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='resultaat',
            name='totaal',
        ),
        migrations.AddField(
            model_name='race',
            name='wedstrijdbaan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='timeteam.Wedstrijdbaan'),
        ),
    ]
