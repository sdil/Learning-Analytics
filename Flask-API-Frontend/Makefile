APP_NAME=Flask-API-Frontend

start:
	docker start -i $(APP_NAME)

create:
	docker run -it --name $(APP_NAME) --link Flask-API -v ~/Project/Flask-API-Frontend:/data -p 81:80  -d alpine /bin/ash

ssh:
	docker exec -it $(APP_NAME) /bin/ash

