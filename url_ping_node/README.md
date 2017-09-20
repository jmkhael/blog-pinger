This sample Python function will connect to a URL over HTTP and return the status code, or give a timeout error.

Happy path:
```
$ curl -d '{"url":"http://jmkhael.io/"}' http://localhost:8080/function/url_ping_node
```

Expected output:
```
{"url":"http://jmkhael.io/","status":"ok","status_code":200}
```

Sad path:
```
$ curl -d '{"url":"http://jmkhael.nok/"}' http://localhost:8080/function/url_ping_node
```

Expected output:
```
{"url":"http://jmkhael.nok/","status":"nok","error":{"code":"ENOTFOUND","errno":"ENOTFOUND","syscall":"getaddrinfo","hostname":"jmkhael.nok","host":"jmkhael.nok","port":80}}
```
