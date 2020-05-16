# foxmask
My Blog with pelican using disqus and providing RSS/ATOM

## Installation

```shell
virtualenv foxmask
cd $_
source bin/activated
git clone https://github.com/foxmask/foxmask.github.io
git clone --recursive https://github.com/getpelican/pelican-plugins
mv foxmask.net website
pip install -r requirements.txt
pelican-theme -s $PWD/pelican-bootstrap3
```

## Ready to create blog post ;)

For that, [go to that link](https://github.com/foxmask/foxmask.github.io/new/master) and enjoy a new post ;)


## Theme pelican-bootstrap3

this one provide tipue_search plugin but this one provide a version of Tipue which is outdated (version 4) and buggy.
version 5 works fine. To install it, just clone https://github.com/Tipue/Tipue-Search, remove from website/output/theme/tipuesearch and, in place of this one,add the tipuesearch coming from the clone you just made.
