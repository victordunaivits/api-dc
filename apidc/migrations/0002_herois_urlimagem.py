# Generated by Django 4.0.5 on 2022-06-29 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apidc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='herois',
            name='urlImagem',
            field=models.CharField(default=123123, max_length=255),
            preserve_default=False,
        ),
    ]