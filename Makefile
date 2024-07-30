
aider-shell:
	docker-compose exec aider bash

build:
	docker-compose build

down:
	docker-compose down

remove-volumes:
	docker-compose down -v

up:
	docker-compose up

shell:
	docker-compose run --rm memefreak bash