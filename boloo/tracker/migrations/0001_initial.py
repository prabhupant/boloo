# Generated by Django 3.0.2 on 2020-01-27 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BillingDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salutation_code', models.CharField(max_length=2)),
                ('first_name', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64)),
                ('street_name', models.CharField(max_length=64)),
                ('house_number', models.CharField(max_length=4)),
                ('zipcode', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=64)),
                ('country_code', models.CharField(max_length=2)),
                ('email', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'billing_detail',
            },
        ),
        migrations.CreateModel(
            name='CustomerDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salutation_code', models.CharField(max_length=2)),
                ('first_name', models.CharField(max_length=64)),
                ('surname', models.CharField(max_length=64)),
                ('street_name', models.CharField(max_length=64)),
                ('house_number', models.CharField(max_length=4)),
                ('zipcode', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=64)),
                ('country_code', models.CharField(max_length=2)),
                ('email', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'customer_detail',
            },
        ),
        migrations.CreateModel(
            name='ShipmentItem',
            fields=[
                ('order_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('order_item_id', models.CharField(max_length=10)),
                ('order_date', models.DateTimeField()),
                ('last_delivery_date', models.DateTimeField()),
                ('ean', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=128)),
                ('quantity', models.IntegerField()),
                ('offer_price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('offer_condition', models.CharField(max_length=10)),
                ('fulfilment_method', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'shipment_item',
            },
        ),
        migrations.CreateModel(
            name='ShipmentItemMapper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment_id', models.IntegerField()),
                ('order_id', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'shipment_item_mapper',
            },
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('transport_id', models.IntegerField(primary_key=True, serialize=False)),
                ('transport_code', models.CharField(max_length=24)),
                ('track_and_trace', models.CharField(max_length=24)),
            ],
            options={
                'db_table': 'transport',
            },
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('shipment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('shipment_date', models.DateTimeField()),
                ('billing_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.BillingDetail')),
                ('customer_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.CustomerDetail')),
                ('shipment_items_mapper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.ShipmentItem')),
                ('transport', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.Transport')),
            ],
            options={
                'db_table': 'shipment',
            },
        ),
    ]
