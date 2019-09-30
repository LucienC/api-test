import requests


# OpenStreetMap utilities


def get_osm_data(region_name, country_name="France", data_format="json"):
    """
    Retrieve data from OSM
    TODO: Improvements
     - Better API connector
     - add retry possibilities
     - Handling error
     - Make it more generic, example: pass data you want to retrieve

    :param region_name:
    :param country_name:
    :param data_format:
    :return:
    """
    api_url = 'https://nominatim.openstreetmap.org/search?'
    params = 'country=' + country_name + '&state=' + region_name + '&format=' + data_format
    try:
        response = requests.get(api_url + params)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise e
    else:
        geodata = response.json()
        return geodata[0] if geodata and geodata[0] else None
