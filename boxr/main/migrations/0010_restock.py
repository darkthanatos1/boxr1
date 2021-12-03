# Generated by Django 3.2.3 on 2021-11-13 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20211102_1825'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.product')),
            ],
        ),
    ]