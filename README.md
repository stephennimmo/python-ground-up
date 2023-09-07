# Python from the Ground Up

Install Poetry: https://python-poetry.org/docs/#installation  



After cloning, run the following commands. 
```
poetry install
poetry shell
```

Add a local .env file
```
DB_USERNAME=postgres
DB_PASSWORD=postgres
DB_HOSTNAME=localhost
DB_PORT=5432
DB_NAME=customer
```

Start the database and run the migration
```
poe compose-up
poe migrate
```

Run the app
```
poe run
```

Run the tests
```
poe test
```

Stop the database
```
poe compose-down
```