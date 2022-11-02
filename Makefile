SHELL := /bin/bash

dev_run: 
	cd api && python manage.py runserver 0.0.0.0:8000
test:
	cd api && python manage.py test

start: dev_run

