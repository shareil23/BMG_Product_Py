# BMG Code Test

BMG Product Exercise.

## Stack
|||
|----|-------|
|Language|Python|
|Framework|Flask|
|Database|Postgres|
|Cache|Redis|
|Container|Docker|
|Port Services Running|`8000`|
|Port Database Running|`7000`|


## Current Directory Structure
```bash
├── README.md
├── app.py
├── Documents
├── docker-compose.yml
├── manage.py
├── migration.sh
├── requirements.txt
└── src
    ├── Config
    ├── Controller
    ├── Models
    ├── Schema
    ├── Static
    ├── Templates
    ├── Test
    ├── InBound
    ├── OutBound
    ├── __init__.py

```

# How To Run The Services

```bash
docker-compose up
```

# How To Destroy The Services

```bash
docker-compose down --rmi local -v
```
