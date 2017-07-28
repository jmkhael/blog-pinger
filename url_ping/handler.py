import requests

def print_url(url):
    try:
        r =  requests.get(url,timeout = 20)
        print(url +" => " + str(r.status_code))
    except:
        print("Timed out trying to reach URL.")
        # download the avatar binary using getavatar function
        requests.post("http://gateway:8080/function/slack_it",
        json = {
            "url": url,
            "status": "nok",
            "message": "failed to ping " + url})

def handle(req):
    print("Handle this -> " + req)
    if req.find("http") == -1:
        print("Give me a URL and I'll ping it for you.")
        return

    print_url(req)

# handle("http://faaster.io")
