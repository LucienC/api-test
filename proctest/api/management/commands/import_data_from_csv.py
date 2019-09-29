from django.core.management.base import BaseCommand
import csv
import time
from django.conf import settings
from django.db import transaction, IntegrityError

from api.models import Region, County, City


class Command(BaseCommand):
    help = 'Populate City, County and Region data from csv.'

    def handle(self, *args, **kwargs):
        # TODO:
        #  - Check data integity
        #  - Add command args for path/file name/delimiter/...
        #  - Better error/exception handling
        #  - Implement re-run functionality

        print("--- Start data import from CSV ---")
        start_time = time.time()

        path = settings.MEDIA_ROOT + 'api/' + 'correspondance-code-insee-code-postal.csv'
        with open(path) as f:
            reader = csv.DictReader(f, delimiter=';')

            regions = []
            departments = []
            cities = []

            for row in reader:
                regions.append((row['Code Région'], row['Région']))
                departments.append((row['Code Département'], row['Département'], row['Code Région']))
                cities.append(
                    (
                        row['Code INSEE'],
                        row['Code Postal'],
                        row['Commune'],
                        row['Population'],
                        row['Superficie'],
                        row['Code Département'],
                        row['Département']

                    )
                )

                # OLD slow method
                #
                # region, created = Region.objects.get_or_create(
                #     code=row['Code Région'],
                #     name=row['Région']
                # )
                #
                # county, created = County.objects.get_or_create(
                #     code=row['Code Département'],
                #     name=row['Département'],
                #     region=region
                # )
                #
                # city, created = City.objects.get_or_create(
                #     code_insee=row['Code INSEE'],
                #     postal_code=row['Code Postal'],
                #     name=row['Commune'],
                #     population=row['Population'],
                #     area=row['Superficie'],
                #     county=county
                # )

        with transaction.atomic():
            try:
                # Bulk import Region data
                Region.objects.bulk_create([Region(code=d[0], name=d[1]) for d in set(regions)])
                region_queryset = Region.objects.all()

                # Bulk import County data
                County.objects.bulk_create(
                    [County(code=d[0], name=d[1], region=region_queryset.get(pk=d[2])) for d in set(departments)])
                county_queryset = County.objects.all()

                # Bulk import City data
                City.objects.bulk_create(
                    [City(code_insee=d[0],
                          postal_code=d[1],
                          name=d[2],
                          population=d[3],
                          area=d[4],
                          county=county_queryset.get(code=d[5], name=d[6])
                          ) for d in set(cities)])
            except IntegrityError as ie:
                # error, rollback
                raise ie
            except Exception as e:
                # error, rollback
                raise e
            else:
                print("--- Data imported in %s seconds ---" % (time.time() - start_time))
