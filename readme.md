# profiler-content

**_TLDR_**: ETL process for SEC's [Financial Statement Data Sets](https://www.sec.gov/dera/data/financial-statement-data-sets.html).

## Description

This project downloads the data sets from [Financial Statement Data Sets](https://www.sec.gov/dera/data/financial-statement-data-sets.html). 

It validates the data as per this [spec](https://www.sec.gov/files/aqfs.pdf) in terms of fields and relations.

Output is persisted to a PostgreSQL database that is employed as input to the [profiler]() project.

Database tables are defined by the schema in the `db_init/postgres/create_tables.sql`. It relaxes some of the constraints defined in the spec because data does not fully live up to its contract.

However, data required for unique keys can be trusted; relevant fields for basic 10-K based fundamental analysis are mostly populated. 

## How to Run

#### Prerequisites
  * If executing for the first time, make sure to create a docker volume beforehand. Name should be `screener-postgres-data`.
  ```shell
  $ docker volume create screener-postgres-data
  ```

  * If you are reexecuting the ETL process for the whole range of years available in the data sets, you'll have to ensure that the database is clean beforehand.
  ```shell
  # Assuming the container have been started with 'docker-compose up -d'
  $ docker exec -it profiler-etl-pgdb /bin/bash
  # Within the postgres container
  > psql -U screeneruser screener_dev
  # Within postgres
  psql> TRUNCATE TABLE submissions CASCADE;
  psql> TRUNCATE TABLE tags CASCADE;
  psql> TRUNCATE TABLE submissions_tmp;
  psql> TRUNCATE TABLE tags_tmp;
  psql> TRUNCATE TABLE numbers_tmp;
  ```
  
#### Executing
1. Start containers
```shell
$ docker-compose up -d
```
2. Get a shell prompt within the `python-etl` container
```shell
$ docker exec -it python-etl /bin/bash
```
3. For full range of years execution
```shell
python ./src/etl.py
```
4. For select range of years execution
```shell
python ./src/etl.py START_YEAR=2012 END_YEAR=2015
```

## TODOS
  * Handle failure to download data gracefully. Currently, when there's a failure to download data from the SEC's website, the ETL process is aborted. File system and database cleanups are not carried out.
  
