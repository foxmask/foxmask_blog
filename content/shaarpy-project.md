Title: ShaarPy Project
Date: 2022-01-20 13:00:00+00:00
Author: FoxMaSk 
Category: link
Tags: ShaarPy, documentation, aide, python, project, opensource
Status: published


# ShaarPy Project

[ShaarPy Project](https://git.afpy.org/foxmask/shaarpy)

### [ShaarPy](https://git.afpy.org/foxmask/shaarpy)

**Share Your Thoughts, Links, Ideas, Notes**

#### Description

This project is a clone of the great [Shaarli](https://sebsauvage.net/wiki/doku.php?id=php:shaarli) made in PHP.
This one is made in [Python](https://www.python.org)3.10 and [Django](https://www.djangoproject.com/) 4.x


#### The features 

##### Notes
- Create *notes* in **Markdown**

##### Links
- Drop a URL and ShaarPy will grab the article page with **image** and **video** if the source website provides ones
&lt;a href=&#34;https://git.afpy.org/foxmask/shaarpy/raw/main/docs/shaarpy_article.png&#34;&gt;&lt;img src=&#34;https://framagit.org/foxmask/shaarpy/-/raw/main/docs/shaarpy_article.png&#34; alt=&#34;article with image&#34; width=&#34;400&#34;/&gt;&lt;/a&gt;

##### Tags
-  Manage tags 
- Tag Cloud

&lt;a href=&#34;https://git.afpy.org/foxmask/shaarpy/raw/main/docs/tags_list.png&#34;&gt;&lt;img src=&#34;https://framagit.org/foxmask/shaarpy/-/raw/main/docs/tags_list.png&#34; alt=&#34;tag cloud&#34; width=&#34;400&#34;/&gt;&lt;/a&gt;

##### Daily links history
- See the links of the day and navigate throw the calendar to go back to your old links

&lt;a href=&#34;https://git.afpy.org/foxmask/shaarpy/raw/main/docs/daily.png&#34;&gt;&lt;img src=&#34;https://framagit.org/foxmask/shaarpy/-/raw/main/docs/daily.png&#34; alt=&#34;daily links&#34; width=&#34;400&#34;/&gt;&lt;/a&gt;

##### Tools
- for each link added, a markdown file can be create in a folder that will be sync on your mobile with the help of &#34;[syncthing](https://syncthing.net/)&#34;
- Import of  **Shaarli** exported bookmark, or even **FireFox** bookmarks
- you can export/import your data in **json** 

**export**
```
python manage.py dumpdata --format json --indent 2 &gt; fixtures/my_shaarpy_dump.json
```

**import**
```
python manage.py loaddata --format json  fixtures/my_shaarpy_dump.json
```

#### Installation

system requirements :

* pandoc

```
apt install pandoc
```

*creation of a python virtualenv*

```
python3 -m venv shaarpy
cd shaarpy
source bin/activate
```


*install the project*

```
git clone https://git.afpy.org/foxmask/shaarpy
cd shaarpy
```

##### Settings

copy the sample config file

```
cp env.sample .env
```

and set the following values

```
# for meta
SHAARPY_NAME=ShaarPy FoxMaSk Links
SHAARPY_DESCRIPTION=Share thoughts, links ideas, notes
SHAARPY_AUTHOR=FoxMaSk
SHAARPY_ROBOT=index, follow
# for MD generation
SHAARPY_LOCALSTORAGE_MD=/home/foxmask/MesNotes/links
SHAARPY_STYLE=blue

SECRET=!DONTFORGETTOCHANGETHISVALUE!

DEBUG=True   # or False in prod
DB_ENGINE=&#39;django.db.backends.sqlite3&#39;
DB_NAME=&#39;db.sqlite3&#39;
DB_USER=&#39;&#39;
DB_PASSWORD=&#39;&#39;
DB_HOST=&#39;&#39;
DB_PORT=&#39;&#39;

TIME_ZONE=&#39;Europe/Paris&#39;
LANGUAGE_CODE=&#39;en-en&#39;
USE_I18N=True
USE_L10N=True
USE_TZ=True
```

#####  Database

*setup the database*

```
cd shaarpy
python manage.py createsuperuser
python manage.py migrate
python manage.py loaddata --format json  fixtures/my_shaarpy_data.json
```

#####  Running the Server

*start the project*

```
python manage.py runserver localhost:8001
```

then, access the project with your browser **http://127.0.0.1:8001/**