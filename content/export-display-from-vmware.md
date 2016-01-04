Title: export DISPLAY from a VMWare virtual machine
Date: 2014-04-17 11:06
Author: foxmask
Category: Techno
Tags: vmware
Slug: export-display-from-vmware
Status: published

I have to install an Oracle server on a remote machine.  
And ... It's not my first time :P

As we need to use a GUI Wizard, usually we do an export of the DISPLAY
to a computer which can handle the X session and then everything works
great... Until now.

I have 2 virtual machine, one with VMWare one with another VM system
(KVM or XEN ; i dont remember ;) both with a CentOS 6.5 with SELinux
disable and no firewalling setup

Both have a role of oracle server.  
My installation on the "non-VMWare" worked fine with the usual process
:

```shell
xhost + new_server
ssh -X -Y login@new_server
export DISPLAY=workstation_ip:0.0
cd /u01/app/oracle/database
./runInstaller 
```

and I received the wizard on my workstation.

Now, with the VMWare Virtual machine, the same process fails when
starting anything that require a X, even xclock for example.

So I compared the ssh config of the both server, to check if the
forwarding is set to on, but are the same.

So I am asking myself if there is no config to set up on the VMWare
virtual machine to permit the X session ?

