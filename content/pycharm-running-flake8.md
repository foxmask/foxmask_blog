Title: PyCharm running Flake8
Date: 2016-02-17 19:00
Author: foxmask
Category: Techno
Tags: pycharm, flake8
Slug: pycharm-running-flake8
Status: published

## The Ugly 

As I like clean things, I like when python tells me that I made ugly things to be able to fix them.

With this in mind, first of all, I used the service [CodeClimate](https://codeclimate.com).
This one permits to tell you where your code can be improved and how.
But the service enters in the game, once the commits are done and pushed on the repository.

As I try to keep the repository as clean as possible, I dont like that : test improvements, commit and push them, get the result from codeclimate, do anoither improvement and so on...


## The Beauty

So I decide to stop that and ask python to tell me where the code need to be improved before any commit.

To do so, as I use [PyCharm 5.1 EAP](https://www.jetbrains.com/pycharm/download/index.html), since a few days, I searched a way to make PyCharm detects and suggests improvements from the opened files.

The code inspection works fine with PEP8, the result of the inspection is automatically displayed in the right margin of the opened file, but it seems there is nothing for Flake8 and McCabe. 

So here is what I did :

* in my virtualenv 

```python
pip install flake8
flake --version
2.5.4 (pep8: *7.0, pyflakes: *0.0, mccabe: 0.4.0) CPython 3.4.2 on Linux
```

* in PyCharm, go to File > Settings > External Tools > click on "+" and fill the fields as below :

[![PyCharm 5 Menu to setup Flake8](/static/2016/02/pycharm_running_flake8_settings.png)](/static/2016/02/pycharm_running_flake8_settings.png)

* once it's done you now have an option in the menu External Tools "Flake8"

[![PyCharm 5 action Flake8](/static/2016/02/pycharm_running_flake8_menu.png)](/static/2016/02/pycharm_running_flake8_menu.png)

* then run it and see in the bottom of the PyCharm window with the "console" to see what's wrong (or not) with the module you've selected

[![PyCharm 5 final result by Flake8](/static/2016/02/pycharm_running_flake8_final_result.png)](/static/2016/02/pycharm_running_flake8_final_result.png)

* if you prefer to run flake8 on the entire folder, change :

```python
--max-complexity 10 $FileDir$/$FileName$
```

by

```python
--max-complexity 10 $FilePath$
```


## Caveats :

May be I went too far and something exists and is much better than this one.

For example, now, if you switch of project, the previous settings remain with the path of the virtualenv we've setup. And if you change the path for the project B, and open project A, the modification from B will remain for A...
As settings for Project do not include this parameter yet, but just "interpreter" and "structure", we are a little bit embarrassed.

## Conclusion :

At least now I'm ready to (try to) make better things ;)
