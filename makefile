drop-db:
	rm -f db.sqlite3

fresh-db: drop-db migrate
	python manage.py createsuperuser --username admin --email admin@example.com

run:
	python manage.py runserver

migrate:
	python manage.py migrate

shell:
	python manage.py shell
