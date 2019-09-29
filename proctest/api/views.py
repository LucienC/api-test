from rest_framework import viewsets

from api.models import Region
from api.paginations import ApiCustomSetPagination
from api.serializers import RegionSerializer


class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint for Region
    """
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    pagination_class = ApiCustomSetPagination
