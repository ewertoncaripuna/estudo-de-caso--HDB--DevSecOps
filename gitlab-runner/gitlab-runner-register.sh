#!/bin/sh
registration_token="GR1348941tgULaU5SydGEc4vajh_B"
url="http://192.168.2.106"

sudo docker exec -it gitlab-runner \
gitlab-runner register \
    --non-interactive \
    --registration-token ${registration_token} \
    --locked=false \
    --description docker-stable \
    --url ${url} \
    --executor docker \
    --docker-image docker:stable \
    --docker-volumes "/var/run/docker.sock:/var/run/docker.sock" \
    --docker-network-mode devSecNetwork
