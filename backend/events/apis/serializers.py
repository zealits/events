from rest_framework import serializers
from .models import VendorTypes, Vendors, VendorSocialMediaHandles,Cities,VendorPhotos

class VendorTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorTypes
        fields = '__all__'

class VendorPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorPhotos
        fields = '__all__'

class VendorSocialMediaHandlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorSocialMediaHandles
        fields = '__all__'

class VendorsSerializer(serializers.ModelSerializer):
    photos = VendorPhotosSerializer(many=True, read_only=True)
    
    class Meta:
        model = Vendors
        fields = '__all__'

class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'
