# Procsea api-test

Backend test

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Clone the repo
```
git clone https://github.com/LucienC/api-test.git .
```

- Create your venv and activate it

```
python -m venv venv
source venv/bin/activate
```

### Installing

- cd to project directory

```
cd proctest
```

- Install requirements
```
pip install -r requirements.txt
```

- Migrate db
```
python manage.py migrate
```

- Populate db from csv, will populate Region, County and City tables
```
python manage.py import_data_from_csv
```

- Populate lat long data of Region model from OpenStreetMap api
```
python manage.py populate_region_data_from_osm
```


- Run server
```
python manage.py runserver
```

Your're good to go : http://127.0.0.1:8000/api/regions/

## Running the tests

```
python manage.py test
```

## Built With

* [Django](https://www.djangoproject.com/)
* [Django REST Framework](https://www.django-rest-framework.org/)

## Authors

* **Lucien CARON**

## Time Spend

env. 4h

## What is buggy

1/ Wasn't really sure what you wanted in the 6th question, call the api on the fly or retrieve data from the api and populate the db?

I started a branch to do it on the fly (osm-on-the-fly) but in this case it is a really bad idea so I didn't spend mutch 
time testing it and instead choose to populate the data in the db using a command :)

2/ I versioned the csv, which is bad, only to facilitate your testing

3/ The data from the csv are not up to date, this is why some region doesn't have lat and long, 
ex: http://127.0.0.1:8000/api/regions/25/

Because open street map don't know BASSE-NORMANDIE anymore.
https://nominatim.openstreetmap.org/search?country=France&state=BASSE-NORMANDIE&format=json

## What could be improved

- More tests
- Better data validation
- ...