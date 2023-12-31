# Generated by Django 4.2.5 on 2023-09-10 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0005_vendorphoto_vendortype_venuephoto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VenuePreferredVendors',
            fields=[
                ('venue_preferred_vendors_id', models.AutoField(primary_key=True, serialize=False)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.vendors')),
                ('vendor_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='apis.vendortype')),
                ('venue', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.venue')),
            ],
            options={
                'db_table': 'venue_vendors',
            },
        ),
    ]
