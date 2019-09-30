from rest_framework import viewsets

from api.models import Region
from api.paginations import ApiCustomSetPagination
from api.serializers import RegionSerializer, RegionListSerializer
from api.utils import get_osm_data


class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for Region
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    pagination_class = ApiCustomSetPagination

    def list(self, request, **kwargs):
        queryset = self.get_queryset()
        region_list = []
        for region in queryset:
            lat_lon = get_osm_data(region.name)
            region.lat = lat_lon['lat']
            region.lon = lat_lon['lon']
            region_list.append(region)
        page = self.paginate_queryset(region_list)
        serializer = RegionListSerializer(page, many=True)

        return self.get_paginated_response(serializer.data)
