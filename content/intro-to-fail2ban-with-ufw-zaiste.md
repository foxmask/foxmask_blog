Title: Intro to fail2ban with ufw - zaiste
Date: 2022-03-06 14:27:51.690384+00:00
Author: FoxMaSk 
Category: link
Tags: fail2ban, security
Status: published




# Intro to fail2ban with ufw - zaiste

[Intro to fail2ban with ufw - zaiste](https://zaiste.net/posts/intro-fail2ban-ufw/)



[fail2ban](https://www.fail2ban.org/wiki/index.php/Main_Page) is
configured by default to only ban failed SSH login attempts. Check the
current configuration with the following command:

    sudo fail2ban-client status

    Status
    |- Number of jail:  1
    `- Jail list:   sshd

Setup
-----

Let\&#39;s start by configuring `fail2ban` to use `ufw` instead of
`iptables`. Verify that there is a `ufw.conf` inside
`/etc/fail2ban/action.d/` directory.

Copy `jail.conf` to `jail.local` to prevent ch...

