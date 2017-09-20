This sample function sends a message to a slack channel

This uses [Botkit](https://www.botkit.ai/). By default it will post to a #blog channel.

You need to specify in the enviroment section a token enabling the function to join your Slack team.

```
  slack_it:
    lang: node
    handler: ./slack_it
    image: jmkhael/faas-slack
    environment:
      token: "xoxb-insert-your-slack-token-here-but-do-not-add-it-to-github"

```

The function will require an input in the form of:
```
$ curl -d '{"message":"Anything really"}' http://localhost:8080/function/slack_it
```

The message can be any json object. It will be forwarded to the Slack channel.

```
$ curl -d '{"message": {"happy": "yes, always!"} }' http://localhost:8080/function/slack_it
```
