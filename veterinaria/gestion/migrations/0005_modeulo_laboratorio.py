# Generated by Django 4.1.3 on 2022-12-27 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0004_programando_Recordatorioss'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordenlaboratoriomodel',
            name='MontoD',
            field=models.FloatField(db_column='MontoD', default=0),
        ),
    ]
