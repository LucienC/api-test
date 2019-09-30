from django.db import models


class Region(models.Model):
    """This class represents the Region model."""
    code = models.CharField(max_length=80, primary_key=True)
    name = models.CharField(max_length=255)
    lat = models.DecimalField(max_digits=9, decimal_places=7, null=True)
    lon = models.DecimalField(max_digits=9, decimal_places=7, null=True)

    @property
    def total_population(self):
        total_population = 0
        departments = self.departments.all()
        for county in departments:
            total_population += county.total_population
        return total_population

    @property
    def total_area(self):
        total_area = 0
        departments = self.departments.all()
        for county in departments:
            total_area += county.total_area
        return total_area

    def __str__(self):
        return "{}".format(self.code, self.name)


class County(models.Model):
    """This class represents the County model."""
    # Code cannot be used as pk, use auto id
    code = models.CharField(max_length=80)
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='departments')

    @property
    def total_population(self):
        total_population = 0
        population_sum = self.cities.aggregate(models.Sum('population'))
        total_population += population_sum["population__sum"]
        return total_population

    @property
    def total_area(self):
        total_area = 0
        area_sum = self.cities.aggregate(models.Sum('area'))
        total_area += area_sum["area__sum"]
        return total_area

    def __str__(self):
        return "{}".format(self.code, self.name)


class City(models.Model):
    """This class represents the City model."""
    code_insee = models.CharField(max_length=80, primary_key=True)
    postal_code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    population = models.FloatField(null=True)
    area = models.FloatField(null=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return "{}".format(self.code_insee, self.name)
