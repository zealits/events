# Generated by Django 4.2.5 on 2023-09-11 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0013_remove_vendors_photos'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendors',
            name='photo',
            field=models.ImageField(default=None, upload_to='vendor_photos/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='VendorPhotos',
        ),
    ]
