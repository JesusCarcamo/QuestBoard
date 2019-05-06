# Generated by Django 2.0.13 on 2019-05-06 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190506_0925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jugador',
            name='amigos',
        ),
        migrations.RemoveField(
            model_name='jugador',
            name='misionesAdquiridas',
        ),
        migrations.RemoveField(
            model_name='jugador',
            name='notificaciones',
        ),
        migrations.AddField(
            model_name='mision',
            name='cazaRecompensas',
            field=models.ManyToManyField(default=None, null=True, related_name='misionesAdquiridas', to='app.Jugador'),
        ),
    ]
