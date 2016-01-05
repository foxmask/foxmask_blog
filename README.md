# foxmask.trigger-happy.eu
My Blog with pelican using disqus and providing RSS/ATOM

## Installation

```shell
virtualenv foxmask.trigger-happy.eu
cd $_
source bin/activated
git clone https://github.com/foxmask/foxmask.trigger-happy.eu
git clone https://github.com/duilio/pelican-octopress-theme.git
git clone --recursive https://github.com/getpelican/pelican-plugins
mv foxmask.trigger-happy.eu website
pip install -r requirements.txt
pelican-theme -s $PWD/pelican-octopress-theme
```

## Ready to create blog post ;)

For that, [go to that link](https://github.com/foxmask/blog.trigger-happy.eu/new/master) and enjoy a new post ;)
