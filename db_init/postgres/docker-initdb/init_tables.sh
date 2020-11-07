#!/bin/bash

set -e

SCREENERUSER_NAME='screeneruser'
SCREENERDEV_DBNAME='screener_dev'

# This assumes the sql script has already been placed in the expected path through
# a shared volume and that the screeneruser has been created and granted privileges
psql -v ON_ERROR_STOP=1 \
     --username "$SCREENERUSER_NAME" \
     --password "$SCREENERUSER_NAME" \
     --dbname "$SCREENERDEV_DBNAME" \
     --echo-all \
     --file "/usr/local/etc/create_tables.sql"

