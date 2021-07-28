Title: Monit ... and more
Date: 2021-07-28 19:00
Author: foxmask
Category: Techno
Tags: python, django, monit
Slug: monit-and-more
Status: published

# Intro

I use monit intensively in my daily pro life, and I plugged that to a django application to always know how the ~300 VM are going.

In that article in the first part, I will describe all the possibilities I found with monit and the second, how to get the results of the probes and put that in a django app.

As I said, as I manage ~300VM, all the installation and configuration of monit is done with 2 ansible playbook, one to install the package, one to set monit and add new probes for all services (like oracle, tomcat, jboss, business services and so on) on each server



# I - Monit



## Install

````
yum install monit
````

or

```shell
apt install monit
```

## Commands

```bash
monit summary
monit status
```

monit allows us to "group" the result of probe with a tag group eg

```bash
monit summary -g server
monit status -g server
```

`monit summary` will render a table ; `monit status` will render the details of each probe 

## Settings

depending on your OS or even version of distribution the config file can be `/etc/monit/monitrc` or `/etc/monit/monit.conf`

### sections of the config file

* run monit each ...

```ini
set daemon 30
```

* limit of various tests

```ini
set limits {
    programOutput:     2 MB,      # check program's output truncate limit
    sendExpectBuffer:  256 B,      # limit for send/expect protocol test
    fileContentBuffer: 512 B,      # limit for file content test
    httpContentBuffer: 1 MB,       # limit for HTTP content test
    networkTimeout:    5 seconds   # timeout for network I/O
    programTimeout:    300 seconds # timeout for check program
    stopTimeout:       30 seconds  # timeout for service stop
    startTimeout:      30 seconds  # timeout for service start
    restartTimeout:    30 seconds  # timeout for service restart
}
```

you will need to change the default value when the `programOutput` will become to be large (with custom pograms for example)

* sending mail

```ini
set mailserver localhost
```

we set the name of the server that will send mail when alerts will occur

* mail content

```ini
set mail-format {
  from:    Monit <monit@$HOST>
  subject: monit alert --  $EVENT $SERVICE
  message: $EVENT Service $SERVICE
                Date:        $DATE
                Action:      $ACTION
                Host:        $HOST
                Description: $DESCRIPTION


            Your faithful employee,
            Monit
--8<--
}
```

this will be the content of the mail that will be send when alerts will occur

* email to receive alert

```ini
set alert john@doe.com not on { instance, action }
```

* allow the http console to be accessing from a browser or curl

```ini
set httpd port 2812 and use address nameoftheserver_or_localhost
    # use address localhost  # only accept connection from localhost (drop if you use M/Monit)
    allow localhost        # allow localhost to connect to the server and
    allow admin:monit      # require user 'admin' with password 'monit'
    #with ssl {            # enable SSL/TLS and set path to server certificate
    #    pemfile: /etc/ssl/certs/monit.pem
    #}
```

* checking system

```ini
check system $HOST
  if loadavg (1min) > 22 for 20 cycles then alert
  if loadavg (5min) > 17 for 20 cycles then alert
  if cpu usage > 95% for 10 cycles then alert
  if memory usage > 75% for 20 cycles then alert
  if swap usage > 25% for 20 cycles then alert
```

* check filesystem

```ini

check filesystem root with path /
    if space usage > 90% then alert
    group server

check filesystem home with path /home
    if space usage > 90% then alert
    group server
```

this will check 2 partitions `/` and `/home`

### checking other services

we can check the existence of the PID file or a process matching a path like as follow

* nginx

```ini
check process nginx with pidfile /var/run/nginx.pid
    start program = "/usr/sbin/service nginx start" with timeout 60 seconds
    stop program = "/usr/sbin/service nginx stop"
    if cpu > 60% for 2 cycles then alert
    if cpu > 80% for 5 cycles then restart
    if totalmem > 200.0 MB for 5 cycles then restart
    if children > 250 then restart
    if disk read > 500 kb/s for 10 cycles then alert
    if disk write > 500 kb/s for 10 cycles then alert
    if failed host localhost port 80 protocol http and request "/index.html" then restart
    if 3 restarts within 5 cycles then unmonitor
    group server
```

* postgresql

```ini
check process postgresql with pidfile /var/lib/pgsql/13/data/postmaster.pid
   start program = "/usr/sbin/service postgresql-13 start"
   stop  program = "/usr/sbin/service postgresql-13 stop"
   if failed host localhost port 5432 protocol pgsql then alert
   group database
```

if the pid file disepears, an alert is raised

* oracle

```ini
check process MYORACLEDB matching "ora_pmon_MYORACLEDB"
   if failed port 1521 then alert
   group database
```

we just check the pmon process and its default 1521 port

* redis

```ini
check process redis matching "/usr/bin/redis-server"
      start program = "/usr/sbin/service redis start"
      stop program = "/usr/sbin/service redis stop"
      if 2 restarts within 3 cycles then timeout
      if totalmem > 100 Mb then alert
      if children > 255 for 5 cycles then stop
      if cpu usage > 95% for 3 cycles then restart
      if failed host 127.0.0.1 port 6379 then restart
      if 5 restarts within 5 cycles then timeout
    group server

check process redis-sentinel matching "/usr/bin/redis-sentinel"
      if failed port 26379 then alert
    group server
```

* jboss and tomcat same thing (except for the match string)

```ini
check process MYJBOSS matching "Djboss.home.dir=/var/lib/MYJBOSS"
      if failed
      port 8082
      for 3 cycles
   then unmonitor
   group appserver
```

we check that a process matches the expected string + check if the port 8082 is opened

* WebSphere

```ini
# check the PID of the appserver
check process BKCFBHD_was with pidfile "/opt/IBM/WebSphere/AppServer/profiles/foxmask/logs/server1/server1.pid"
      if failed
      port 9093
      for 3 cycles
   then unmonitor
   group appserver
```

* checking a django project

```ini
check process myproject with pidfile '/home/foxmask/Projects/nyuseu/gunicorn_nyuseu.pid'
    if failed port 8001 for 2 cycles then alert
    group server
```

* running "a ping" to check if one of my 'server' is still here

```ini
check host the_name_i_want_for_my_probe with address anotherserver
   if failed ping then alert  # IPv4 or IPv6
   every "0,5,10,15,20,25,30,35,40,45,50,55 8-19 * * *"
   group server
```

### custom mail alert content

you may want to receive email with few of more details from a given probe that return an alert. Here is an example to send an alert with a different 'default' format we saw earlier.

```ini
check host partner_server with address partner.company1.com
    if failed
        port 443 protocol https
        and request /GAMES/ with content = "Login"
    then alert

    alert joe.doe@company0.com
    alert jane.doe@company0.com
       with mail-format {
            from: IT_Support@company.com
            subject: [$HOME] partner.company1.com does not respond $DATE
            message: The application at the URL https://check host partner_server with address partner.company1.com/GAMES/ is unavailable
       }
    every "13 8-19 * * 1-5"
    group server

```

thus here, each 13 min from 8h to 19h from Monday to Friday, the server partner.company1.com is checked and if the https://partner.company1.com/GAMES/ is not found, raise an alert send to joe and jane with the given 

#### sending alert to a Slack channel

```ini
check host server101 with address server101
    if failed ping then exec "/home/foxmask/scripts/slack.sh" else if succeeded then exec "/home/foxmask/scripts/slack.sh"
    alert joe.doe@company0.com
    alert jane.doe@company0.com
      with mail-format {
           from: DL_CFTech@se.linedata.com
           subject:  the server server101 server-tfsf-prdapp02 does not respond $DATE
           message:  Ping has failed to server server101 $DATE
      }
   every "0,5,10,15,20,25,30,35,40,45,50,55 8-19 * * *"
   group server
```

`slack.sh` will look like this 

```ini
set -e
set -u

URL=https://hooks.slack.com/services/<THE ID OR YOUR CUSTOM HOOK>

if test -z $URL
then
        >&2 echo "No Slack webhook URL provided"
        exit 1
fi

CHANNEL=projet
STATUS=${MONIT_EVENT:-unknown}
SERVICE=${MONIT_SERVICE:-?}

PAYLOAD="{
        \"channel\": \"#${CHANNEL:-alerts}\",
        \"username\": \"Monit\",
        \"icon_emoji\": \":robot_face:\",
        \"attachments\": [{
                \"fallback\": \"${SERVICE} – ${MONIT_DESCRIPTION:-?}\",
                \"mrkdwn_in\": [\"pretext\"],
                \"pretext\": \"*${SERVICE}*\",
                \"text\": \"${MONIT_DESCRIPTION:-?}\",
                \"color\": \"${MONIT_COLOR:-$([[ $STATUS == *"succeeded"* ]] && echo good || echo danger)}\",
                \"fields\": [
                        { \"title\": \"Date\", \"value\": \"${MONIT_DATE:-$(date -R)}\", \"short\": true },
                        { \"title\": \"Host\", \"value\": \"${MONIT_HOST:-$(hostname)}\", \"short\": true },
                        { \"title\": \"Service\", \"value\": \"${SERVICE}\", \"short\": true },
                        { \"title\": \"Status\", \"value\": \"${STATUS}\", \"short\": true }
                ]}
        ]
}"

curl -s -X POST --data-urlencode "payload=$PAYLOAD" $URL
```

(source [https://peteris.rocks/blog/monit-configuration-with-slack/](https://peteris.rocks/blog/monit-configuration-with-slack/))

in the previous example, "group server", "group database" allow us to requests status of probe grouped by this keyword, for exemple :

```shell
$ monit summary -g server
$ monit status -g server
$ monit status -g database
```



# II - Django application



After all those configuration, 

* I made a management command that will read the "Servers" model
* run curl -XGET http://login:pass@server/_status?format=xml for each server
* convert the XML into a dict (thanks to xmltodict)
* update the data (probes) of the server into the database



`models.py`

a model a little bit long with manager with a `Service` models that matches all monit use case.

```python
# coding: utf-8
from django.db import models


class Server(models.Model):

    """
        Server
    """
    name = models.CharField(max_length=200, unique=True)
    watch = models.BooleanField(default=True)
    swap_limit = models.IntegerField()
    cpu_limit = models.IntegerField()
    vm = models.BooleanField(default=False)

class ServicesQS(models.QuerySet):

    def ok(self):
        return self.filter(status=True)

    def ko(self):
        return self.filter(status=False)

    def system(self):
        return self.filter(type="System")

    def system_ok(self):
        return self.filter(type="System", status=True)

    def system_ko(self):
        return self.filter(type="System", status=False)

    def filesystem(self):
        return self.filter(type="FileSystem")

    def filesystem_ok(self):
        return self.filter(type="FileSystem", status=True)

    def file_system_ko(self):
        return self.filter(type="FileSystem", status=False)

    def network(self):
        return self.filter(type="Network")

    def network_ok(self):
        return self.filter(type="Network", status=True)

    def network_ko(self):
        return self.filter(type="Network", status=False)

    def files(self):
        return self.filter(type="Files")

    def files_ok(self):
        return self.filter(type="Files", status=True)

    def files_ko(self):
        return self.filter(type="Files", status=False)

    def directory(self):
        return self.filter(type="Directory")

    def directory_ok(self):
        return self.filter(type="Directory", status=True)

    def directory_ko(self):
        return self.filter(type="Directory", status=False)

    def host(self):
        return self.filter(type="Host")

    def host_ok(self):
        return self.filter(type="Host", status=True)

    def host_ko(self):
        return self.filter(type="Host", status=False)

    def process(self):
        return self.filter(type="Process")

    def process_ok(self):
        return self.filter(type="Process", status=True)

    def process_ko(self):
        return self.filter(type="Process", status=False)

    def services(self):
        return self.filter(type="Services")

    def services_ok(self):
        return self.filter(type="Services", status=True)

    def services_ko(self):
        return self.filter(type="Services", status=False)


class ServicesMgr(models.Manager):
    def get_queryset(self):
        return ServicesQS(self.model, using=self._db)  # Important!

    def ok(self):
        return self.get_queryset().ok()

    def ko(self):
        return self.get_queryset().ko()

    def system(self):
        return self.get_queryset().system()

    def system_ok(self):
        return self.get_queryset().system_ok()

    def system_ko(self):
        return self.get_queryset().system_ko()

    def file_system(self):
        return self.get_queryset().filesystem()

    def filesystem_ok(self):
        return self.get_queryset().filesystem_ok()

    def filesystem_ko(self):
        return self.get_queryset().file_system_ko()

    def network(self):
        return self.get_queryset().network()

    def network_ok(self):
        return self.get_queryset().network_ok()

    def network_ko(self):
        return self.get_queryset().network_ko()

    def files(self):
        return self.get_queryset().files()

    def files_ok(self):
        return self.get_queryset().files_ok()

    def files_ko(self):
        return self.get_queryset().files_ko()

    def directory(self):
        return self.get_queryset().directory()

    def directory_ok(self):
        return self.get_queryset().directory_ok()

    def directory_ko(self):
        return self.get_queryset().directory_ko()

    def host(self):
        return self.get_queryset().host()

    def host_ok(self):
        return self.get_queryset().host_ok()

    def host_ko(self):
        return self.get_queryset().host_ko()

    def process(self):
        return self.get_queryset().process()

    def process_ok(self):
        return self.get_queryset().process_ok()

    def process_ko(self):
        return self.get_queryset().process_ko()

    def services(self):
        return self.get_queryset().services()

    def services_ok(self):
        return self.get_queryset().services_ok()

    def services_ko(self):
        return self.get_queryset().services_ko()


class Services(models.Model):
    """
        Service
    """
    name = models.CharField(max_length=200)
    server = models.ForeignKey(Server, blank=True, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)
    status = models.BooleanField()
    status_string = models.TextField()
    data_collected = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=10, null=True)

    objects = ServicesMgr()  # manager to get the status ok/ko



class MonitServers(models.Model):

    """
        MonitServer
    """

    server = models.OneToOneField(
        Server,
        related_name="monit",
        on_delete=models.CASCADE,
        null=True
    )
    monit_user = models.CharField(max_length=10)
    monit_pass = models.CharField(max_length=20)
    monit_ip = models.CharField(max_length=40)
    monit_port = models.IntegerField()

```

`admin.py`

```python
from django.contrib import admin

from monitoring.models import Server, Services, MonitServers

class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'vm', 'swap_limit', 'cpu_limit')
    ordering = ['name']
    fields = ('name', 'watch', 'swap_limit', 'cpu_limit', 'vm')

    search_fields = ['name']

    class Meta:
        ordering = ['name']


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'server', 'status', 'data_collected')
    ordering = ['type', 'name']
    search_fields = ['name', 'server__name']


class MonitServersAdmin(admin.ModelAdmin):
    list_display = ('server', 'monit_user', 'monit_ip', 'monit_port')
    ordering = ['server']
    search_fields = ['server__name']

    
admin.site.register(Server, ServerAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(MonitServers, MonitServersAdmin)
```

`management/commands/monit.py `

```python
# coding: utf-8
from datetime import datetime
from django.core.management.base import BaseCommand
from logging import getLogger
from monitoring.models import Server, MonitServers
from rich.console import Console
import xmltodict


# create logger
logger = getLogger('monitoring.monit')

console = Console()
console_warning = "bold yellow"
console_danger = "bold red"
console_info = "blue"
console_success = "green"


def get_monit_json(monit_obj):
    """
	get the status of the server
    :param server:
    :param monit_ip:
    :return: stats in json
    """
    allstat = {'monit': {}}
    url = "http://{monit_ip}:{monit_port}/_status?format=xml".format(monit_ip=monit_obj.monit_ip,
                                                                     monit_port=monit_obj.monit_port)
    console.print(monit_obj.monit_ip, url, style=console_info)
    try:
        res = requests.get(url, auth=(monit_obj.monit_user, monit_obj.monit_pass))
        if res.status_code == 200:
            try:
                allstat = json.loads(json.dumps(xmltodict.parse(res.text)))
            except xml.parsers.expat.ExpatError as e:
                logger_error.error(e)
                console.print(e, style=console_warning)
    except requests.ConnectionError as e:
        logger_error.error(e)
        console.print(e, style=console_warning)

    return allstat['monit']


def server_check_service(allstat):
    """

    :return:
    """
    # server info
    server_memory = round(float(int(allstat['platform']['memory']) / 1024 / 1024), 2)
    server_swap = round(float(int(allstat['platform']['swap']) / 1024 / 1024), 2)
    # services
    services = allstat['service']
    # read the service returned by the curl for example

    for service in services:
        # type = FileSystem
        if service['@type'] == '0':
            programs = add_filesystem(programs, service)
        # type = directory
        elif service['@type'] == '1':
            programs = add_dir(programs, service)
        # type = file
        elif service['@type'] == '2':
            programs = add_files(programs, service)
        # type = process
        elif service['@type'] == '3':
            programs = add_process(programs, service)
        # type = host
        elif service['@type'] == '4':
            programs = add_hosts(programs, service)
        # type = info Operating System
        elif service['@type'] == '5':
            programs = add_os(programs, service, server_memory, server_swap)
        # type = 'custom probe' not covered in that blog post ;)
        # elif service['@type'] == '7':
        #  [...]
    return programs
          

class Command(BaseCommand):

    help = 'Check the status of the servers'

    def add_arguments(self, parser):
        parser.add_argument('server',
                            type=str,
                            help='server name or "ALL"')

    def handle(self, *args, **options):
        """

        """
        console.print("Begin : Check services", style=console_success)
        if options.get('server') == 'ALL':
            servers = Server.objects.all()
        else:
            servers = Server.objects.filter(name=options.get('server'))
            if len(servers) == 0:
                log = "server {server} not found".format(server=options.get('server'))
                console.print(log, style=console_danger)
        for line in servers:
            
            log = "Reresh data of {line}".format(line=line)
            console.print(log, style=console_info)
            
            monit_obj, created = MonitServers.objects.get_or_create(
                server=line,
                defaults={'monit_user': 'admin',
                          'monit_pass': 'monit',
                          'monit_ip': '127.0.0.1',
                          'monit_port': 2812},
            )
            programs = get_monit_json(monit_obj)
            if len(programs) == 0:
                trace = "Getting services from {server} failed from " \
                        "http://{monit_user}:***@{monit_ip}:{monit_port}/_status?format=xml"
                trace = trace.format(server=monit_obj,
                                     monit_user=monit_obj.monit_user,
                                     monit_ip=monit_obj.monit_ip,
                                     monit_port=monit_obj.monit_port)
                logger_error.error(trace)
                console.print(trace, style=console_danger)
                return       

            if programs:
                for program in programs:
                    log = "{} {} {} {}".format(line.name, program['name'], program['status'], program['status_string'])
                    logger.debug(log)
                    # [...]
                    # update Services model
        console.print("End : Check services", style=console_success)

```

this command will launch a curl for each server which will requests  the "monit" data then will convert XML to Dict and then update the model `Service`

`views.py`

a short view which display the list of services by server + the details of all service for the choosen server

```python
# coding: utf-8
from django.db.models import Count
from django.views.generic import ListView, DetailView
from monitoring.models import Server


class Home(ListView):
    """
        Home page
    """
    context_object_name = "servers_list"
    template_name = 'monitoring/home.html'
    model = Server

    def get_queryset(self):
        return Server.objects.annotate(num_services=Count('services')).filter(num_services__gt=0).order_by('name')



class MonitoringServerDetail(DetailView):
    """
        Detail page of a server
    """
    model = Server
    slug_field = 'name'
    template_name = 'monitoring/server_detail.html'

    def get_queryset(self):
        return Server.objects.filter(name=self.kwargs['slug'])


```

`templates/monitoring/home.html`

that page will display all the server and the status of each probe

```html
{% extends "base.html" %}
{% load static %}
{% block title %}Server Monitoring{% endblock %}
{% block menu_left %}
{% endblock %}
{% block bootstrap_css %}
<!-- CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
{% endblock %}
{% block content %}
    <div class="col-lg-12 col-md-12">
      <h1>Monitoring - <small class="text-muted">Server status</small></h1>
      <div class="row row-cols-4 row-cols-md-4">
        {% for server in servers_list %}
            <div class="card-deck mb-3">
                <div class="card">
                    <div class="card-body">
                      <div class="card_title">
                          <h5><a title="View details of server" href="{% url 'monitoring_server_detail' server.name %}">{{ server.name }}</a></h5>
                      </div>
                      <div class="card-text">
                      <table class="table table-hover">
                        <tbody>
                          <tr><td>System</td><td class="
                            {% if server.services_set.system_ok.count > 0 and server.services_set.system_ko.count == 0 %}table-success
                            {% elif server.services_set.system_ok.count > 0 and server.services_set.system_ko.count > 0 %}table-warning
                            {% elif server.services_set.system_ok.count == 0 and server.services_set.system_ko.count == 0 %}table-secondary
                            {% else %}table-danger{% endif %}
                            "> </td></tr>
                          <tr><td>Filesystem</td><td class="
                            {% if server.services_set.filesystem_ok.count > 0 and server.services_set.filesystem_ko.count == 0 %}table-success
                            {% elif server.services_set.filesystem_ok.count > 0 and server.services_set.filesystem_ko.count > 0 %}table-warning
                            {% elif server.services_set.filesystem_ok.count == 0 and server.services_set.filesystem_ko.count == 0 %}table-secondary
                            {% else %}table-danger{% endif %}"> </td></tr>
                          <tr><td>File</td><td class="
                            {% if server.services_set.files_ok.count > 0 and server.services_set.files_ko.count == 0 %}table-success
                            {% elif server.services_set.files_ok.count > 0 and server.services_set.files_ko.count > 0 %}table-warning
                            {% elif server.services_set.files_ok.count == 0 and server.services_set.files_ko.count == 0 %}table-secondary
                            {% else %}table-danger{% endif %}"> </td></tr>
                          <tr><td>Directory</td><td class="
                            {% if server.services_set.directory_ok.count > 0 and server.services_set.directory_ko.count == 0 %}table-success
                            {% elif server.services_set.directory_ok.count > 0 and server.services_set.directory_ko.count > 0 %}table-warning
                            {% elif server.services_set.directory_ok.count == 0 and server.services_set.directory_ko.count == 0 %}table-secondary
                            {% else %}table-danger{% endif %}"> </td></tr>
                          <tr><td>Network</td><td class="
                            {% if server.services_set.network_ok.count > 0 and server.services_set.network_ko.count == 0 %}table-success
                            {% elif server.services_set.network_ok.count > 0 and server.services_set.network_ko.count > 0 %}table-warning
                            {% elif server.services_set.network_ok.count == 0 and server.services_set.network_ko.count == 0 %}table-secondary
                            {% else %}table-danger{% endif %}"> </td></tr>
                          <tr><td>Host</t><td class="
                            {% if server.services_set.host_ok.count > 0 and server.services_set.host_ko.count == 0 %}table-success
                            {% elif server.services_set.host_ok.count > 0 and server.services_set.host_ko.count > 0 %}table-warning
                            {% elif server.services_set.host_ok.count == 0 and server.services_set.host_ko.count == 0 %}table-secondary
                            {% else %}table-danger{% endif %}"> </td></tr>
                          <tr><td>Services</td><td class="
                            {% if server.services_set.services_ok.count > 0 and server.services_set.services_ko.count == 0 %}table-success
                            {% elif server.services_set.services_ok.count > 0 and server.services_set.services_ko.count > 0 %}table-warning
                            {% elif server.services_set.services_ok.count == 0 and server.services_set.services_ko.count == 0 %}table-secondary
                            {% else %}table-danger{% endif %}"> </td></tr>
                          <tr><td>Process</td><td class="
                            {% if server.services_set.process_ok.count > 0 and server.services_set.process_ko.count == 0 %}table-success
                            {% elif server.services_set.process_ok.count > 0 and server.services_set.process_ko.count > 0 %}table-warning
                            {% elif server.services_set.process_ok.count == 0 and server.services_set.process_ko.count == 0 %}table-secondary
                            {% else %}table-danger{% endif %}"> </td></tr>
                          </tbody>
                        </table>
                      </div>
                    </div>                    
                </div>
            </div>
        {% endfor %}
        </div>       
        <span class="badge btn btn-success"> all is ok </span>
        <span class="badge btn btn-warning"> some services are ko </span>
        <span class="badge btn btn-danger "> all is ko </span>
        <span class="badge btn btn-secondary"> non monitored </span>
    </div>
{% endblock %}
{% block bootstrap_js %}
<!-- jQuery and JS bundle w/ Popper.js -->
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>
{% endblock bootstrap_js %}

```

that page will display the status details of one server 

`templates/monitoring/server_detail.html`

```html
{% extends "base.html" %}
{% block title %}Service monitoring - {{ object }}{% endblock %}
{% block menu_left %}
{% endblock %}
{% block content %}
<div class="col-sm-12 col-md-12">
  <a href="{% url 'monitoring_home' %}" class="glyphicon glyphicon-arrow-left btn btn-success"> Retour</a>
  <div class="thumbnail">
    <div class="caption">
      <h3><span class="glyphicon glyphicon-tasks"></span> {{ server.name }}</h3>
      <div>
        <ul class="nav nav-tabs" role="tablist">
          <li role="presentation" class="active"><a href="#system_{{ server.name }}" aria-controls="system_{{ server.name }}" role="tab" data-toggle="tab"><span class="glyphicon glyphicon-hdd"></span> System</a></li>
          <li role="presentation"><a href="#filesystem_{{ server.name }}" aria-controls="fileystem_{{ server.name }}" role="tab" data-toggle="tab"><span class="glyphicon glyphicon-list"></span> FileSystem</a></li>
          <li role="presentation"><a href="#file_{{ server.name }}" aria-controls="file_{{ server.name }}" role="tab" data-toggle="tab"><span class="glyphicon glyphicon-list"></span> File</a></li>
          <li role="presentation"><a href="#directory_{{ server.name }}" aria-controls="directory_{{ server.name }}" role="tab" data-toggle="tab"><span class="glyphicon glyphicon-folder-open"></span> Directory</a></li>
          <li role="presentation"><a href="#network_{{ server.name }}" aria-controls="network_{{ server.name }}" role="tab" data-toggle="tab"><span class="glyphicon glyphicon-signal"></span> Network</a></li>
          <li role="presentation"><a href="#host_{{ server.name }}" aria-controls="host_{{ server.name }}" role="tab" data-toggle="tab"><span class="glyphicon glyphicon-home"></span> Host</a></li>
          <li role="presentation"><a href="#process_{{ server.name }}" aria-controls="process_{{ server.name }}" role="tab" data-toggle="tab"><span class="glyphicon glyphicon-home"></span> Process</a></li>
          <li role="presentation"><a href="#services_{{ server.name }}" aria-controls="services_{{ server.name }}" role="tab" data-toggle="tab"><span class="glyphicon glyphicon-retweet"></span> Services</a></li>
        </ul>
      </div>
      <div class="tab-content">
        {% include "monitoring/probes.html" with probe_name="system" server_name=server.name services_ko=server.services_set.system_ko services_ok=server.services_set.system_ok %}
        {% include "monitoring/probes.html" with probe_name="filesystem" server_name=server.name services_ko=server.services_set.filesystem_ko services_ok=server.services_set.filesystem_ok %}
        {% include "monitoring/probes.html" with probe_name="file" server_name=server.name services_ko=server.services_set.file_ko services_ok=server.services_set.files_ok %}
        {% include "monitoring/probes.html" with probe_name="directory" server_name=server.name services_ko=server.services_set.directory_ko services_ok=server.services_set.directory_ok %}
        {% include "monitoring/probes.html" with probe_name="network" server_name=server.name services_ko=server.services_set.network_ko services_ok=server.services_set.network_ok %}
        {% include "monitoring/probes.html" with probe_name="host" server_name=server.name services_ko=server.services_set.host_ko services_ok=server.services_set.host_ok %}
        {% include "monitoring/probes.html" with probe_name="services" server_name=server.name services_ko=server.services_set.services_ko services_ok=server.services_set.services_ok %}
        {% include "monitoring/probes.html" with probe_name="process" server_name=server.name services_ko=server.services_set.process_ko services_ok=server.services_set.process_ok %}
      </div>
    </div>
  </div>
</div>
{% endblock %}
{% block extrajs %}
<script type="text/javascript">
//<![CDATA[
$(document).ready(function() {
    $('[data-toggle="tooltip"]').tooltip()
    $('[data-toggle="popover"]').popover()
    $('li.connection-top').hide()
    setTimeout(function() {
        $('p.connection-middle').slideUp("slow", function() {
            $('li.connection-top').show("slow")
        });
    }, 4000);
});
//]]>
</script>
{% endblock extrajs %}


```

`templates/monitoring/probes.html`

```html
<div role="tabpanel" class="tab-pane fade {% if probe_name == 'system' %} in active {% endif %}" id="{{ probe_name }}_{{ server_name }}">
  <table class="table table-striped table-hover">
    <tbody>
    {% for service in services_ko %}
    <tr class="table-success">
      <td>{{ service.name }}</td>
      <td>
        <button type="button" class="btn btn-lg btn-danger" data-toggle="tooltips" title="{{ service.status_string }}"><span class="glyphicon glyphicon-minus-sign"></span></button>
      </td>
    </tr>
    {% endfor %}
    {% for service in services_ok %}
    <tr class="table-danger">
      <td>{{ service.name }}</td>
      <td>
        <button type="button" class="btn btn-lg btn-success" data-toggle="tooltips" title="{{ service.status_string }}"><span class="glyphicon glyphicon-ok-sign"></span></button>
      </td>
    </tr>
    {% endfor %}
    </tbody>
  </table>
</div>
```



And , *That's all Folks!!*

