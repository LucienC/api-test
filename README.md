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
