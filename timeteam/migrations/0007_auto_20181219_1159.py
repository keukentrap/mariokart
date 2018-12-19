# Generated by Django 2.1.4 on 2018-12-19 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timeteam', '0006_auto_20181219_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultaat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('split1', models.IntegerField(blank=True)),
                ('totaal', models.IntegerField(blank=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='coureur',
            options={'ordering': ['rugnummer']},
        ),
        migrations.AddField(
            model_name='resultaat',
            name='coureur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timeteam.Coureur'),
        ),
        migrations.AddField(
            model_name='resultaat',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timeteam.Race'),
        ),
    ]
