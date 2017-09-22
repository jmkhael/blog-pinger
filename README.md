# blog-pinger

This repository is an [OpenFaaS](https://github.com/alexellis/faas) stack I use to ping my blog and report back on a slack channel if the ping fails.

This has an accompanying blog post you can find here: http://jmkhael.io/downnotifier-site-pinger/

## TLDR;

1. Adapt the token in samples.yml as specified in [slack_it](slack_it/README.md)
2. build and deploy
```
./build.sh
./deploy.sh http://jmkhael.io
```

3. Test the individual functions `./test.sh`

If everything works fine, you should see something like the below.

```
{"url":"http://jmkhael.io/","status":"ok","status_code":200}
Initializing Botkit v0.5.6
info: ** No persistent storage method specified! Data may be lost when process shuts down.
info: ** Setting up custom handlers for processing Slack messages
info: ** API CALL: https://slack.com/api/chat.postMessage
{"slackit":"v1","request":{"message":"Anything really"}}
{"DownNotifier":"v1","request":{"url":"http://jmkhael.io"},"response":"all ok - slack not informed"}
```

4. Profit!
