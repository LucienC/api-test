from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from api.models import Region
from api.serializers import RegionSerializer


class GetAllRegionsTest(APITestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        Region.objects.create(code=1, name='region 1')
        Region.objects.create(code=2, name='region 2')
        Region.objects.create(code=3, name='region 3')
        Region.objects.create(code=4, name='region 4')

    def test_get_all_regions(self):
        url = reverse('regions-list')
        response = self.client.get(url, format='json')
        regions = Region.objects.all()
        serializer = RegionSerializer(regions, many=True)
        # have to use data['results'] instead of data because of the custom region pagination ApiCustomSetPagination
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
