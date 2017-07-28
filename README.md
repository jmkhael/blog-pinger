# blog-pinger
FaaS stack to ping my blog and report on a slack channel if ping fails

1. Deploy faas
2. Deploy docker-compose (cron)
3. Adapt the token in samples.yml

4. build and deploy
```
./build.sh
./deploy.sh
```
5. `./test.sh`
