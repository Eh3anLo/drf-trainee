#!/bin/bash
# wait-for-postgres.sh

set -e

until pg_isready -h "$POSTGRES_HOST" -p "$POSTGRES_PORT"; do
  echo "Waiting for Postgres to be ready..."
  sleep 2
done
