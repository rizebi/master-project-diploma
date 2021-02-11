#/bin/bash

IP=192.168.64.2
PORT=80
HOST_NAME=dizertatie.com
PRODUCTION_VERSION=1
CANARY_VERSION=2

COUNT_PRODUCTION=0
COUNT_CANARY=0

for i in {1..100}; do
  RESPONSE=$(curl -s -H "Host: ${HOST_NAME}" ${IP}:${PORT} | grep ${PRODUCTION_VERSION})
  if [[ "x${RESPONSE}" == "x" ]]; then
    # This means that the request was handled by CANARY
    COUNT_CANARY=$((COUNT_CANARY+1))
  else
    # This means that the request was handled by PRODUCTION
    COUNT_PRODUCTION=$((COUNT_PRODUCTION+1))
  fi
done

echo "Production version (${PRODUCTION_VERSION}) was served for ${COUNT_PRODUCTION} times"
echo "Canary version (${CANARY_VERSION}) was served for ${COUNT_CANARY} times"