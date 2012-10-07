#!/bin/bash
pushd ~/hjemmeside

if [ -f django.pid ]; then
	kill $(cat django.pid)
	rm -f django.pid
fi

python manage.py runfcgi method=prefork host=127.0.0.1 port=10005 --settings=settings pidfile=django.pid

popd

