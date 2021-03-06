# Generated by Django 2.0.13 on 2019-05-06 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='amigos',
            field=models.ManyToManyField(null=True, related_name='_jugador_amigos_+', to='app.Jugador'),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='misionesAdquiridas',
            field=models.ManyToManyField(null=True, related_name='cazaRecompensas', to='app.Mision'),
        ),
        migrations.AlterField(
            model_name='jugador',
            name='notificaciones',
            field=models.ManyToManyField(null=True, to='app.Notificacion'),
        ),
    ]
