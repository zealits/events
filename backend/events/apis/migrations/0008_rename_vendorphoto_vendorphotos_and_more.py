# Generated by Django 4.2.5 on 2023-09-10 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0007_remove_vendors_email_remove_venue_photos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VendorPhoto',
            new_name='VendorPhotos',
        ),
        migrations.RenameModel(
            old_name='VendorType',
            new_name='VendorTypes',
        ),
        migrations.RenameModel(
            old_name='VenuePhoto',
            new_name='VenuePhotos',
        ),
        migrations.RenameModel(
            old_name='Venue',
            new_name='Venues',
        ),
        migrations.RenameModel(
            old_name='SocialMediaHandles',
            new_name='VenueSocialMediaHandles',
        ),
        migrations.RenameModel(
            old_name='VenueType',
            new_name='VenueTypes',
        ),
        migrations.AlterModelTable(
            name='venuesocialmediahandles',
            table='venue_s_m_handles',
        ),
        migrations.CreateModel(
            name='VendorSocialMediaHandles',
            fields=[
                ('social_media_handle_id', models.AutoField(primary_key=True, serialize=False)),
                ('facebook_url', models.URLField(blank=True, default=None, max_length=255, null=True)),
                ('instagram_url', models.URLField(blank=True, default=None, max_length=255, null=True)),
                ('twitter_url', models.URLField(blank=True, default=None, max_length=255, null=True)),
                ('linkedin_url', models.URLField(blank=True, default=None, max_length=255, null=True)),
                ('youtube_url', models.URLField(blank=True, default=None, max_length=255, null=True)),
                ('vendor', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='apis.vendors')),
            ],
            options={
                'db_table': 'vendor_s_m_handles',
            },
        ),
    ]