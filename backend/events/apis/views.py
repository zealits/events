from rest_framework import viewsets
from .models import VendorTypes, Vendors, VendorSocialMediaHandles, VendorPhotos,Cities
from .serializers import VendorTypesSerializer, VendorsSerializer, VendorSocialMediaHandlesSerializer, VendorPhotosSerializer,CitiesSerializer

class VendorTypesViewSet(viewsets.ModelViewSet):
    queryset = VendorTypes.objects.all()
    serializer_class = VendorTypesSerializer


class VendorSocialMediaHandlesViewSet(viewsets.ModelViewSet):
    queryset = VendorSocialMediaHandles.objects.all()
    serializer_class = VendorSocialMediaHandlesSerializer

class VendorPhotosViewSet(viewsets.ModelViewSet):
    queryset = VendorPhotos.objects.all()
    serializer_class = VendorPhotosSerializer

class VendorsViewSet(viewsets.ModelViewSet):
    queryset = Vendors.objects.all()
    serializer_class = VendorsSerializer

class CitiesViewSet(viewsets.ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer