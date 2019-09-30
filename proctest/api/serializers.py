from rest_framework import serializers
from api.models import Region


class RegionSerializer(serializers.ModelSerializer):
    totalPopulation = serializers.CharField(source='total_population')
    totalArea = serializers.CharField(source='total_area')

    class Meta:
        model = Region
        fields = ('code', 'name', 'totalPopulation', 'totalArea', 'lat', 'lon')
