Title: CentOs Oracle Could not open/read file:///etc/pki/rpm-gpg/RPM-GPG-KEY-oracle
Date: 2014-10-17 08:36
Author: foxmask
Category: Techno
Tags: centos, oracle
Slug: centos-oracle-could-not-openread-fileetcpkirpm-gpgrpm-gpg-key-oracle
Status: published

Quand on a besoin de faire un `yum update` suivi d'un
`yum install foobar` il peut arriver que sur votre CentOS vous ayez un
problème avec vos packages Oracle :

```shell
warning: rpmts_HdrFromFdno: Header V3 RSA/SHA256 Signature, key ID ec551f03: NOKEY
Retrieving key from file:///etc/pki/rpm-gpg/RPM-GPG-KEY-oracle


GPG key retrieval failed: [Errno 14] Could not open/read file:///etc/pki/rpm-gpg/RPM-GPG-KEY-oracle
```

Pour y remédier 2 commandes et puis s'en va

```shell
[root@localhost ~]# rpm --import http://oss.oracle.com/ol6/RPM-GPG-KEY-oracle
[root@localhost ~]# rpm -q gpg-pubkey-ec551f03-4c2d256a
```

et au yum install suivant tout glisse.

[source](https://community.oracle.com/thread/3539099?start=0&tstart=0)

