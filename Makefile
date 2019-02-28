NAMEWEB   := 127.0.0.1:5000/trivagodemo
NAMESQL   := 127.0.0.1:5000/trivagomysql
TAG       := $$(git log -1 --pretty=%h)
IMGWEB    := ${NAMEWEB}:${TAG}
IMGSQL    := ${NAMESQL}:${TAG}
LATESTWEB := ${NAMEWEB}:latest
LATESTSQL := ${NAMESQL}:latest

init: setup build-web build-mysql push-web push-mysql swarm

.PHONY : init

setup:
	@docker swarm init
	@docker service create --name registry --publish published=5000,target=5000 registry:2

test:
	@docker-compose up -d

test-stop:
	@docker-compose down --volumes

build-web:
	@docker build -t ${IMGWEB} app/.
	@docker tag ${IMGWEB} ${LATESTWEB}

build-mysql:
	@docker build -t ${IMGSQL} mysql/.
	@docker tag ${IMGSQL} ${LATESTSQL}

push-web:
	@docker push ${NAMEWEB}

push-mysql:
	@docker push ${NAMESQL}
swarm:
	@docker stack deploy --compose-file docker-compose.yml trivagodemo

deploy-app:
	@docker service update --image ${NAMEWEB} web

test-web:
	@curl -H Host:web.trivago.kb http://127.0.0.1

destroy-all:
	@docker stack rm trivagodemo
	@docker service rm registry
	@docker swarm leave --force