import requests
import rx
import json
from rx import Observable, Observer

class MyObserver(Observer):
    def __init__(self, url):
        self.url = url

    def on_next(self, x):
        print("Got: %s" % x)

    def on_error(self, e):
        error = "%s" % e
        print(error)
        requests.post("http://gateway:8080/function/slack_it",
            json = {
                "url": self.url,
                "status": "nok",
                "error" : error,
                "message": "failed to ping " + self.url})

    def on_completed(self):
        print("Sequence completed")

def print_url(url):
    result = None
    #try:
    #    r =  requests.get(url,timeout = 20)
    #    result = url +" => " + str(r.status_code)
    #    print(result)
    #except:
    #    print("Timed out trying to reach URL.")
    #    requests.post("http://gateway:8080/function/slack_it",
    #    json = {
    #        "url": url,
    #        "status": "nok",
    #        "message": "failed to ping " + url})

    print("Handle this -> " + url)
    r =  requests.get(url,timeout = 20)
    result = {"result": url +" => " + str(r.status_code)}
    #print(result)
    print(json.dumps(result))

    return result

def handle(req):

    #print("Handle this -> " + req)
    if req.find("http") == -1:
        print("Give me a URL and I'll ping it for you.")
        return

    xs = Observable.defer(lambda: Observable.of(req).map(lambda x: print_url(x)).delay(2000).retry(3)).subscribe(MyObserver(req))

    #print_url(req)
