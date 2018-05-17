Title: Wallabag API 1.0.1
Date: 2016-04-22 20:00
Author: foxmask
Category: Techno
Tags: TriggerHappy, Wallabag, python
Slug: wallabag-api-1.0.1
Status: published

# Intro

This API is like a story of old friends for me, destinies that cross and intersect.

Something like 10 years ago, I met [@nicosomb](https://twitter.com/nicosomb) on http://punbb.fr, a french community arround PunBB, 
where I was administrator.

After all that years, Nicolas made the PHP opensource project named "poche" at first, which became [Wallabag](https://www.wallabag.org/), 
when on my side, after years, I stopped participating on [Jelix, a PHP5 framework](http://jelix.org), for Python.

Then, when I started [TriggerHappy](https:/github.com/push-things/django-th/) and could integrate Pocket successfully,
I asked to Nicolas If he planed to make an API that I then could integrate too... That was 2 years ago ;)

Today, Wallabag is now in version 2 and the API is ready. Thanks to him and to his wonderful team. 
So I finally could finish the [Python API](https://github.com/foxmask/wallabag_api) on my side too.

And now there is no more barrier to each of us to host our own Wallabag and TriggerHappy instance for our own pleasure ;)

# How to create a post in wallabag ?

Here is a snipset to create a entry in your wallabag account :

```python
from wallabag_api.wallabag import Wallabag
# settings
params = {'username': 'foxmask',
          'password': 'mypass',
          'client_id': 'myid',
          'client_secret': 'mysecret'}
my_host = 'http://localhost:8080'
# get token
token = Wallabag.get_token(host=my_host, **params)

# create a post
wall = Wallabag(host=my_host, client_secret='mysecret', client_id='myid', token=token)

my_url = 'https://blog.trigger-happy.eu'
my_title = 'Trigger Happy blog'
my_tags = ['python', 'wallabag']

wall.post_entries(url=my_url, title=my_title, tags=my_tags)
```

this will give you something like this 

![wallabag post](https://raw.githubusercontent.com/foxmask/wallabag_api/master/wallabag.png)
