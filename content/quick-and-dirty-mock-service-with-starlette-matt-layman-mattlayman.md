Title: Quick and dirty mock service with Starlette · Matt Layman - mattlayman
Date: 2022-02-04 16:01:12.566028+00:00
Author: FoxMaSk 
Category: link
Tags: starlette, webhook
Status: published


# Quick and dirty mock service with Starlette · Matt Layman - mattlayman

[Quick and dirty mock service with Starlette · Matt Layman - mattlayman](https://www.mattlayman.com/blog/2019/starlette-mock-service/)

I had a challenge at work. The team needed to mock out a third party
service in a testing environment. The service was slow and configuring
it was painful. If we could mock it out, then the team could avoid those
problems.

The challenge with mocking out the service is that part of the flow
needs to invoke a webhook that will call back to my company&#39;s system to
indicate that all work is done. Addi...
