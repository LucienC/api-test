from django.test import TestCase
from api.models import Region, County, City


class RegionModelTest(TestCase):
    """ Test module for Region model """

    def setUp(self):
        Region.objects.create(code='1', name='RegionTest1')
        Region.objects.create(code='2', name='RegionTest2')

    def test_region_code(self):
        region_1 = Region.objects.get(code='1')
        region_2 = Region.objects.get(code='2')
        self.assertEqual(region_1.code, '1')
        self.assertEqual(region_2.code, '2')


class CountyModelTest(TestCase):
    """ Test module for County model """

    def setUp(self):
        region_1 = Region.objects.create(code='1', name='RegionTest1')

        County.objects.create(code="1", name='CountyTest1', region=region_1)
        County.objects.create(code="2", name='CountyTest2', region=region_1)

    def test_county_code(self):
        county_1 = County.objects.get(code='1')
        county_2 = County.objects.get(code='2')
        self.assertEqual(county_1.code, '1')
        self.assertEqual(county_2.code, '2')

    def test_county_region(self):
        county_1 = County.objects.get(code='1')
        county_2 = County.objects.get(code='2')
        self.assertEqual(county_1.region, Region.objects.get(code='1'))
        self.assertEqual(county_2.region, Region.objects.get(code='1'))


class CityModelTest(TestCase):
    """ Test module for City model """

    def setUp(self):
        region_1 = Region.objects.create(code='1', name='RegionTest1')
        county_1 = County.objects.create(code="1", name='CountyTest1', region=region_1)

        City.objects.create(code_insee='123B',
                            postal_code='22500',
                            name='Paimpol',
                            population=156.87,
                            area=2222.2,
                            county=county_1)
        City.objects.create(code_insee='123C',
                            postal_code='35000/35200/35700',
                            name='Rennes',
                            population=15552.0,
                            area=3535.2,
                            county=county_1)

    def test_city_code_insee(self):
        city_1 = City.objects.get(code_insee='123B')
        city_2 = City.objects.get(code_insee='123C')
        self.assertEqual(city_1.code_insee, '123B')
        self.assertEqual(city_2.code_insee, '123C')

    def test_city_county(self):
        city_1 = City.objects.get(code_insee='123B')
        city_2 = City.objects.get(code_insee='123C')
        self.assertEqual(city_1.county, County.objects.get(code="1", name='CountyTest1'))
        self.assertEqual(city_2.county, County.objects.get(code="1", name='CountyTest1'))
