# **RelyComply Social Media Coding Task**

#### Problem

Our client, Morgain Stainley, needs an API with live data on the activity levels of different social networks to serve as an input to their AI trading bots. Specifically, they need an API they can query to get a numeric indicator for each social network to feed into the neural network of their trading models. This should be a quick little task, but the client is paying us a billion dollars so your implementation needs to be robust.

#### Solution

We’ve found some very simple endpoints to obtain this data from (don’t tell the client!):

- [https://takehome.io/twitter](https://takehome.io/twitter)
- [https://takehome.io/facebook](https://takehome.io/facebook)
- https://takehome.io/instagram

(Let's pretending it's 10 years ago and Facebook hasn't yet bought Instagram.)

Complete the Flask server in `app.py` so that it will return a JSON response with a indicator of the activity level for each social network. Something along the lines of `{"instagram": ..., "facebook": ..., "twitter": ...}`.

If you are in doubt of a detail of the spec just use your best judgement and let me know what you decided with the submission.

#### Caveat

Because some of these social networks adopted the slogan *"Move fast and break things"*, they don't always respond predictably. They break. And respond with invalid JSON. Life's hard.

#### 

#### Quickstart

To get the project up and running, clone the repo and run:

```
pip install -r requirements.txt
flask --debug run
```



