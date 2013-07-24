#!/bin/bash

while true; do
  find . -iname '*.py' | xargs inotifywait -q -e CLOSE_WRITE
  sleep 1
  ./manage.py test "$@"
done
