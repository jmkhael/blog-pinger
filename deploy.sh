
export URL=$1
if [ -z "$URL" ]
then
      echo "You didn't pass a url to the script, defaulting to http://jmkhael.io"
      export URL="http://jmkhael.io"
fi

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
    wget http://gateway:8080/function/down_notifier --post-data='{"url" : "'$URL'"}'

faas-cli -action deploy -f ./samples.yml
