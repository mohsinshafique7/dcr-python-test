# Digital Control Room - Python Test

Thank you for thaking the time to complete this exercise.

## Introduction

Please clone (don't fork) this repository, complete the exercises below and then upload to a public repository on github and send us the link.

Please don't spend more than 2 hours on this task (not including initial download and setup). If you reach 2 hours, please commit your code as-is to your repository.

## Project Setup

You will need python3.8+ to run this code.

```bash
git clone git@github.com:<TBC>

cd dcr-python-test
git remote remove origin
git remote add origin <Your Repository>

cd src
python3 list_countries.py
```

## Exercises

### Exercise 1 - Add Stats

Please add a script that will provide aggregated stats for each region. The stats should contain:

- The region's name
- The number of countries in that region (a simple count)
- The total population of the region (the sum of the population of each country)

The output should be JSON with a format:

```json
{
    "regions": [
        {
        "name": "Africa",
        "number_countries": xxx,
        "total_population": xxx
        },
        {
        "name": "Americas",
        "number_countries": xxx,
        "total_population": xxx
        },
        ...
    ]
}
```

### Exercise 2 - Integrate with API

The script:

```bash
python load_data.py
```

currently populates the database from a local JSON file. Please update this management command to obtain the JSON input data from this url: `https://storage.googleapis.com/dcr-django-test/countries.json`

### Exercise 3 - Store additional Data

The previous script:

```bash
python load_data.py
```

currently extracts and stores the data:

- name
- alpha2Code
- alpha3Code
- population
- region

Please update the database tables and management command to also import:

- topLevelDomain
- capital

Please record any SQL commands executed to modify the database schema.

## Solution Documentation:

#### New File: list_region.py

This file prints and returns data in the following JSON format:

```json
{
    "regions": [
        {
        "name": "Africa",
        "number_countries": xxx,
        "total_population": xxx
        },
        {
        "name": "Americas",
        "number_countries": xxx,
        "total_population": xxx
        },
        ...
    ]
}
```

#### Updated File: load_data.py

The load_data.py script has been updated to fetch data from an API using the request library.

**Updated File: db.py**

In the insert method of the db.py file, additional fields topLevelDomain and capital have been added to handle the insertion of additional data. The list_all method is also updated accordingly to handle retrieval of newly added data.

### Additional Scripts:

- **delete_data.py**: Deletes previous data from tables and creates a new table.
- **create_table.py**: This script creates a new table in the database.

### Usage:

1. Clone the repository.
2. Navigate to the src directory.
3. Run `python list_region.py` to return JSON data and print it.
4. Run `python load_data.py` to load data from the API.
5. Run `python delete_data.py` to delete data from all tables.
6. Run `python create_table.py` to create tables if they don't exist

These updates provide enhanced functionality for handling data, including fetching from APIs, managing additional fields, and creating new tables
