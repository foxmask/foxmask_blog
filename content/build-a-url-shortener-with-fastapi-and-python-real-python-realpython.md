Title: Build a URL Shortener With FastAPI and Python – Real Python - realpython
Date: 2022-05-27 21:59:42.200192+00:00
Author: FoxMaSk 
Tags: python
Status: published
Category: link




# Build a URL Shortener With FastAPI and Python – Real Python - realpython

[Build a URL Shortener With FastAPI and Python – Real Python - realpython](https://realpython.com/build-a-python-url-shortener-with-fastapi/)

# Build a URL Shortener With FastAPI and PythonReal Python

par Real Python, le mercredi 18 mai 2022 16:00

In this tutorial, you’ll build a URL shortener with Python and FastAPI. URLs can be extremely long and not user-friendly. This is where a URL shortener can come in handy. A URL shortener reduces the number of characters in a URL, making it easier to read, remember, and share. 

By following this step-by-step project, you’ll build a URL shortener with Python and FastAPI. At the end of this tutorial, you’ll have a fully functional API-driven web app that creates shortened URLs that forward to target URLs. 

In this tutorial, you’ll learn how to: 

• Create a REST API with FastAPI

• Run a development web server with Uvicorn

• Model an SQLite database

• Investigate the auto-generated API documentation

• Interact with the database with CRUD actions

• Optimize your app by refactoring your code 

This URL shortener project is for intermediate Python programmers who want to try out FastAPI and learn about API design, CRUD, and interaction with a database. To follow along, it’ll help if you’re familiar with the basics of handling HTTP requests. If you need a refresher on FastAPI, Using FastAPI to Build Python Web APIs is a great introduction. 

Get Source Code: Click here to get access to the source code that you’ll use to build your Python URL shortener with FastAPI. 

Demo: Your Python URL Shortener 

In this step-by-step project, you’ll build an API to create and manage shortened URLs. The main purpose of this API is to receive a full target URL and return a shortened URL. To try out your API endpoints, you’ll leverage the documentation that FastAPI automatically creates: 

When you post a target URL to the URL shortener app, you get a shortened URL and a secret key back. The shortened URL contains a random key that forwards to the target URL. You can use the secret key to see the shortened URL’s statistics or delete the forwarding. 

Project Overview 

Your URL shortener Python project will provide API endpoints that are capable of receiving different HTTP request types. Each endpoint will perform an action that you’ll specify. Here’s a summary of your URL shortener’s API endpoints: 

/admin/{secret_key} DELETE Your secret key Deletes your shortened URL