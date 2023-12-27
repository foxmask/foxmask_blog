# foxmask
My Blog with pelican providing RSS/ATOM

## Installation

```shell
python3 -m venv foxmask.eu.org
cd $_
source bin/activate
git clone https://github.com/foxmask/foxmask.github.io
git clone https://github.com/foxmask/foxmask_blog
cd foxmask_blog
pip install -r requirements.txt

git clone https://github.com/alexandrevicenzi/Flex
pelican-themes -s $PWD/Flex
```

## Ready to create blog post ;)

For that, [go to that link](https://github.com/foxmask/foxmask.github.io/new/master) and enjoy a new post ;)

or add content into foxmask_blog/content then enter make html

the Makefile use the path ../foxmask.github.io/ to add content there

## Theme used: Flex

https://pelicanthemes.com/Flex/
