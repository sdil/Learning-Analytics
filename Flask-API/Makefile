APP_NAME=Flask-API

create:
	docker run -it --name Flask-API -v ~/Project/Flask-API:/data -p 80:80 -d python 

ssh:
	docker exec -it $(APP_NAME) /bin/bash

get-ip:
	docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(APP_NAME)

start:
	docker start $(APP_NAME) 
	docker exec -it $(APP_NAME) /bin/bash

db:
	docker exec -it Flask-API mysql -uroot -proot

