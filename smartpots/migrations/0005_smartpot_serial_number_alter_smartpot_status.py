# Generated by Django 5.1.1 on 2024-11-02 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartpots', '0004_alter_smartpot_plant_alter_smartpot_pot_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='smartpot',
            name='serial_number',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='smartpot',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Inactivo'), (1, 'Bueno'), (2, 'Advertencia'), (3, 'En peligro')], default=0),
        ),
    ]
