docker stack deploy -c docker-compose.yml func

sleep 10

docker service rm cronjob
docker service create --name cronjob \
    --network func_functions --replicas 0 \
    --restart-condition=none \
    -l "com.df.notify=true" \
    -l "com.df.cron=true" \
    -l "com.df.cron.name=cronjob" \
    -l "com.df.cron.image=alpine" \
    -l "com.df.cron.command=echo Hello World" \
    -l "com.df.cron.schedule=@every 10s" \
    alpine \
    wget http://gateway:8080/function/down_notifier --post-data='{"url" : "http://jmkhael.io"}'

faas-cli -action deploy -f ./samples.yml
