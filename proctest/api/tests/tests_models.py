from django.test import TestCase
from api.models import Region, County, City


class RegionModelTest(TestCase):
    """ Test module for Region model """

    @classmethod
    def setUpTestData(cls):
        cls.region_1 = Region.objects.create(code='1', name='RegionTest1')
        cls.region_2 = Region.objects.create(code='2', name='RegionTest2')

    def setUp(self):
        pass

    def test_region_code(self):
        self.assertEqual(self.region_1.code, '1')
        self.assertEqual(self.region_2.code, '2')

    def test_region_name(self):
        self.assertEqual(self.region_1.name, 'RegionTest1')
        self.assertEqual(self.region_2.name, 'RegionTest2')


class CountyModelTest(TestCase):
    """ Test module for County model """

    @classmethod
    def setUpTestData(cls):
        cls.region_1 = Region.objects.create(code='1', name='RegionTest1')
        cls.county_1 = County.objects.create(code="1", name='CountyTest1', region=cls.region_1)
        cls.county_2 = County.objects.create(code="2", name='CountyTest2', region=cls.region_1)

    def setUp(self):
        pass

    def test_county_code(self):
        self.assertEqual(self.county_1.code, '1')
        self.assertEqual(self.county_2.code, '2')

    def test_county_region(self):
        self.assertEqual(self.county_1.region, self.region_1)
        self.assertEqual(self.county_2.region, self.region_1)


class CityModelTest(TestCase):
    """ Test module for City model """

    @classmethod
    def setUpTestData(cls):
        cls.region_1 = Region.objects.create(code='1', name='RegionTest1')
        cls.county_1 = County.objects.create(code="1", name='CountyTest1', region=cls.region_1)
        cls.city_1 = City.objects.create(code_insee='123B',
                                         postal_code='22500',
                                         name='Paimpol',
                                         population=156.87,
                                         area=2222.2,
                                         county=cls.county_1)

        cls.city_2 = City.objects.create(code_insee='123C',
                                         postal_code='35000/35200/35700',
                                         name='Rennes',
                                         population=15552.0,
                                         area=3535.2,
                                         county=cls.county_1)

    def setUp(self):
        pass

    def test_city_code_insee(self):
        self.assertEqual(self.city_1.code_insee, '123B')
        self.assertEqual(self.city_2.code_insee, '123C')

    # etc...

    def test_city_county(self):
        self.assertEqual(self.city_1.county, self.county_1)
        self.assertEqual(self.city_2.county, self.county_1)
