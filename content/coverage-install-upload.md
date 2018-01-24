Title: Coverage, install, upload results
Date: 2017-10-14 17:00
Author: foxmask
Category: Techno
Tags: test, coverage, python
Slug: coverage-install-upload-results
Status: published
Summary: Creating coverage report, I put that here, as a reminder for a later use.

# Installation of Coverage


```python
pip install coverage
```

running on a django project :


# Running coverage

```python
coverage run --source='.'  ./manage.py test -v2
coverage html
coverage report
```

# Publishing the results with covveralls.io

On https://coveralls.io/github/foxmask/django-th get the token, then install

```python
pip install python-coveralls
```
Now the command `coveralls` is available

As I don't use Travis (but not in pro) and don't have private repo, I don't put the token in a .coveralls.yml at all, so to share the result we use the command line :


```python
COVERALLS_REPO_TOKEN=_the_long_string_of_the_token coveralls
INFO:coveralls:200
INFO:coveralls:{"message":"Job ##1.1","url":"https://coveralls.io/jobs/30251510"}
```
If you go back to coveralls.io, you will find the job and the result of the coverage

Then add the following to your README.rst (for example) 

```rst
.. image:: https://coveralls.io/repos/github/foxmask/django-th/badge.svg
    :target: https://coveralls.io/github/foxmask/django-th
```

# End

Ready to go !


