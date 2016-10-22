Title: UnitTest, Coverage and Mock
Date: 2016-10-21 20:00
Author: foxmask
Category: Techno
Tags: test, coverage, mock, python
Slug: test-coverage-mock
Status: published
Summary: Today, I will show you the way to mock "service" in your UnitTest processing. As usual, I make things simples, like a rookie would discovered it.

# Introduction 

When we write unittest, it comes the moment when we cross the road of some services that we can't test.
So the moment comes when we have to use [Mock](https://docs.python.org/dev/library/unittest.mock.html)

In the following text, you should spot some evidence related to django ;)

# Function to mock


here is the piece of code I will "mock" :


```python

    def save_data(self, trigger_id, **data):
        """
            let's save the data

            :param trigger_id: trigger ID from which to save data
            :param data: the data to check to be used and save
            :type trigger_id: int
            :type data:  dict
            :return: the status of the save statement
            :rtype: boolean
        """
        status = False
        # set the title and content of the data
        title, content = super(ServiceTwitter, self).save_data(
            trigger_id, **data)

        if data.get('link') and len(data.get('link')) > 0:

            content = str("{title} {link}").format(
                title=title, link=data.get('link'))

            content += self.get_tags(trigger_id)

            try:
                self.twitter_api.update_status(status=content)
                status = True
            except Exception as inst:
                logger.critical("Twitter ERR {}".format(inst))
                update_result(trigger_id, msg=inst)
                status = False
        return status
```

## Mock a complet function

the piece of unittest with the mock applied to `save_data` :
    
```python
    from unittest.mock import patch
    
    def test_save_data(self):
        token = self.token
        trigger_id = self.trigger_id
        content = 'foobar #tag'
        self.data['title'] = 'a title'
    self.data['link'] = 'http://domain.ltd'

        self.assertTrue(token)
        self.assertTrue(isinstance(trigger_id, int))
        self.assertIn('text', self.data)
        self.assertNotEqual(self.data['text'], '')

        with patch.object(ServiceTwitter, 'save_data') as mock_save_data:
            se = ServiceTwitter(self.token)
            se.save_data(trigger_id, **self.data)
        mock_save_data.assert_called_once_with(trigger_id, **self.data)
```


then the testing show us 

```
coverage run --source='.' manage.py test -v2
...
test_save_data (th_twitter.tests.ServiceTwitterTest) ... ok
...
```
Fine !

But the coverage report (in html) shows us 

![Twitter mocking save_data](https://foxmask.trigger-happy.eu/static/twitter_mock_save_data.png)


and the % 
```
[foxmask:~/DjangoVirtualEnv/django-trigger-happy/django-th] [django-trigger-happy] coverage report -m |grep twitter
th_twitter/__init__.py                                2      0   100%   
th_twitter/forms.py                                  12      0   100%   
th_twitter/models.py                                 21      0   100%   
th_twitter/my_twitter.py                            117     56    52%   119-121, 138-173, 190-209, 219-231, 241-250, 256, 273-278
th_twitter/tests.py                                  80      0   100%   
   
```        

## Mock one FunctionB in a FunctionA 

It's fine, but in our quest of the perfect tests and to be sharper, we would like to test the content of `save_data` and only mock the function that makes the call to the Twitter API (named Twython).

To do so we can use the manager like previously, or a decorator. 

Just have a look :

               
```python
    from unittest.mock import patch            
               

    @patch.object(Twython, 'update_status')
    def test_save_data(self, mock1):
        self.create_twitter()
        token = self.token
        trigger_id = self.trigger_id
        content = 'foobar #tag'
        self.data['title'] = 'a title'
        self.data['link'] = 'http://domain.ltd'

        self.assertTrue(token)
        self.assertTrue(isinstance(trigger_id, int))
        self.assertIn('text', self.data)
        self.assertNotEqual(self.data['text'], '')

        se = ServiceTwitter(self.token)
        se.save_data(trigger_id, **self.data)
        mock1.assert_called_once_with(status=content)
```

And this time the coverage report show us 

![Twitter mocking save_data](https://foxmask.trigger-happy.eu/static/twitter_mock_save_data2.png)


and the % 
```
[foxmask:~/DjangoVirtualEnv/django-trigger-happy/django-th] [django-trigger-happy] coverage report -m |grep twitter
th_twitter/__init__.py                                2      0   100%   
th_twitter/forms.py                                  12      0   100%   
th_twitter/models.py                                 21      0   100%   
th_twitter/my_twitter.py                            117     40    66%   119-121, 138-173, 205-208, 241-250, 256, 273-278
th_twitter/tests.py                                  80      0   100%   
```

## Mock (2 or more functions) FunctionB and FunctionC in a FunctionA

Let's suppose you want to mock several functions in `save_data`, we will do something like this :

```python
    from unittest.mock import patch            
               
    # be careful with the order of the decorator 
    @patch.object(Twython, 'update_status')  # will go to mock2
    @patch.object(AnotherService, 'other_method')  # will go to mock1
    def test_save_data(self, mock1, mock2):
        self.create_twitter()
        token = self.token
        trigger_id = self.trigger_id
        content = 'foobar #tag'
        self.data['title'] = 'a title'
        self.data['link'] = 'http://domain.ltd'

        self.assertTrue(token)
        self.assertTrue(isinstance(trigger_id, int))
        self.assertIn('text', self.data)
        self.assertNotEqual(self.data['text'], '')

        se = ServiceTwitter(self.token)
        se.save_data(trigger_id, **self.data)
        mock1.assert_called_once_with()  
        mock2.assert_called_once_with(status=content)
```

/!\ Here, be really very carefull with the order of the decorator: 

if the parms for Twython.update_status and AnotherService.other_method are the same, we can write twice the same like `mock1.assert_called_once(status=content)` and `mock2.assert_called_once(status=content)` (for example)
but if they don't, be sure to set the right parm to the right 'mock'

# End

Hope this will be helpful like it was for me as I spent a lot of time to find and test that ;)

If you want to dig that topic [have a look at the doc](https://docs.python.org/dev/library/unittest.mock.html#patch-object)
