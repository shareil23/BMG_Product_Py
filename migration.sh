#!/bin/sh

chmod u+x migration.sh

if [ "$1" -eq first ]; then
  flask db init
  flask db migrate
  flask db upgrade
else
  flask db migrate
  flask db upgrade
fi