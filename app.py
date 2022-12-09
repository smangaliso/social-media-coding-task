from flask import Flask
import json, threading, time
from urllib import request

app = Flask(__name__)

json_response = {}


def get_activity(name, url):
    try:
        request_site = request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = request.urlopen(request_site).read()
        dict_ = json.loads(data)
        time.sleep(2)
        json_response[name] = dict_
    except Exception as ex:
        pass


@app.route("/")
def social_network_activity():
    get_instagram_activity = threading.Thread(target=get_activity, args=("instagram", "https://takehome.io/instagram"))

    get_facebook_activity = threading.Thread(target=get_activity, args=("facebook", "https://takehome.io/facebook"))

    get_twitter_activity = threading.Thread(target=get_activity, args=("twitter", "https://takehome.io/twitter"))

    # start the threads
    get_instagram_activity.start()
    get_facebook_activity.start()
    get_twitter_activity.start()

    # join the threads
    get_instagram_activity.join()
    get_facebook_activity.join()
    get_twitter_activity.join()

    return json_response
