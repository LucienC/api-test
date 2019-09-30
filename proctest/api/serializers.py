from rest_framework import serializers
from api.models import Region


class RegionListSerializer(serializers.Serializer):
    code = serializers.CharField()
    name = serializers.CharField()
    totalPopulation = serializers.CharField(source='total_population')
    totalArea = serializers.CharField(source='total_area')
    lat = serializers.CharField()
    lon = serializers.CharField()


class RegionSerializer(serializers.ModelSerializer):
    totalPopulation = serializers.CharField(source='total_population')
    totalArea = serializers.CharField(source='total_area')

    class Meta:
        model = Region
        fields = ('code', 'name', 'totalPopulation', 'totalArea')
