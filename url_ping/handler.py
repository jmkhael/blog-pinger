import logging
import logging.config
import requests
import rx
import json
from rx import Observable, Observer

class MyObserver(Observer):
    def __init__(self, url):
        self.url = url

    def on_next(self, x):
        #print("Got: %s" % x)
        pass

    def on_error(self, e):
        error = "%s" % e
        result = {
            "url": self.url,
            "status": "nok",
            "error" : error,
            "message": "failed to ping " + self.url
            }

        print(json.dumps(result))

    def on_completed(self):
        #print("Sequence completed")
        pass

def print_url(url):
    r =  requests.get(url,timeout = 20)
    result = {
        "url": url,
        "status":"ok",
        "status_code": str(r.status_code)
    }
    print(json.dumps(result))

    return result

def handle(req):
    logging.config.dictConfig({
    'version': 1,
    # Other configs ...
    'disable_existing_loggers': True
    })

    url = None
    try:
        url = json.loads(req)['url'];

        if url.find("http") == -1:
            print("Give me a json with a url field, and I'll ping it for you.")
            return

        xs = Observable.defer(lambda: Observable.of(url).map(lambda x: print_url(x)).delay(2000).retry(3)).subscribe(MyObserver(url))
    except:
        print("Give me a json with a url field, and I'll ping it for you.")
