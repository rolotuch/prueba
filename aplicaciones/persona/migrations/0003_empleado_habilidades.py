# Generated by Django 3.1.4 on 2021-01-05 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_auto_20210105_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(to='persona.Habilidades'),
        ),
    ]
