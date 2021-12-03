# Generated by Django 3.2.3 on 2021-10-12 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carton_QTY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('color_id', models.IntegerField(primary_key=True, serialize=False)),
                ('color_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('GTIN_number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('carton_qty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.carton_qty')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.color')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('size_id', models.IntegerField(primary_key=True, serialize=False)),
                ('size_name', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('style_id', models.IntegerField(primary_key=True, serialize=False)),
                ('style_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product_On_Pallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('pallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.pallet')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.size'),
        ),
        migrations.AddField(
            model_name='product',
            name='style',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.style'),
        ),
        migrations.AddField(
            model_name='pallet',
            name='product',
            field=models.ManyToManyField(through='main.Product_On_Pallet', to='main.Product'),
        ),
    ]
