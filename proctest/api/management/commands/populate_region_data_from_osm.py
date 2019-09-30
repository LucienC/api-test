from django.core.management.base import BaseCommand
import time
from django.db import transaction, IntegrityError
from api.models import Region
from api.utils import get_osm_data


class Command(BaseCommand):
    help = 'Populate Region lat,long data from OpenStreetMap api.'

    def handle(self, *args, **kwargs):
        # TODO: Improvements
        #  - Check data integity
        #  - Better error/exception handling
        #  - Add args to choose what data to import from OSM

        print("--- Start data import from OSM Api ---")
        start_time = time.time()

        with transaction.atomic():
            try:
                # Get all existing regions in db
                region_queryset = Region.objects.all()
                for region in region_queryset:
                    # Get data from OSM for current region
                    lat_lon = get_osm_data(region.name)
                    # Update lat long data
                    if lat_lon:
                        region.lat = lat_lon['lat']
                        region.lon = lat_lon['lon']
                        region.save()
            except IntegrityError as ie:
                # error, rollback
                raise ie
            except Exception as e:
                # error, rollback
                raise e
            else:
                print("--- Data imported in %s seconds ---" % (time.time() - start_time))
