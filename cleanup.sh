docker service rm cronjob
faas-cli remove --yaml=./samples.yml
docker stack rm func
