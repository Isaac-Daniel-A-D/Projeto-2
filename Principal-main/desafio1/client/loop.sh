#!/bin/sh
# Cliente de monitoramento
set -e

echo "Iniciando monitoramento do servidor..."

while true; do

  TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

  RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" http://server:8080/status)

  if [ "$RESPONSE" -eq 200 ]; then
      echo "[$TIMESTAMP] [INFO] Healthcheck OK - Server responded 200"
  else
      echo "[$TIMESTAMP] [ERROR] Connection Failed - Status: $RESPONSE"
  fi

  sleep 3
done