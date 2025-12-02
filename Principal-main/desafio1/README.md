docker network create net-monitoramento

docker build -t server-api ./desafio1/server
docker build -t client-monitor ./desafio1/client

docker run -d --name server --network net-monitoramento -p 8080:8080 server-api

docker run -d --name client --network net-monitoramento client-monitor

docker logs -f client