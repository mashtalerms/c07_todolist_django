#!/bin/bash
python todolist/manage.py collectstatic --no-input -v 1
python todolist/manage.py migrate --check
status=$?
if [[ $status != 0 ]]; then
  python todolist/manage.py migrate
fi

exec "$@"