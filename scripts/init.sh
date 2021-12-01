#!/bin/bash
j2 db.sql.j2 -o db.sql
PGPASSWORD=$password psql -U $user -h $host -d $db < db.sql
