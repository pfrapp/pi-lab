# pi-lab
Projects with my RPi 4

## Scope

This repo is mainly a collection of issues I encountered
and their solution
to make the life of future me easier.

If it helps someone else -- great.

## OS versions

Raspberry Pi OS (or Raspbian) is based on Debian.
Those are the version I worked with so far
* Buster (for quite some time -- perhaps too long)
* Bullseye (not really, only for one day after the long overdue update)
* Bookworm (current setup)

Note that the networking configuration changed quite a bit between
bullseye and bookworm.
Since bookworm, you use `nmcli` to configure networking
(this is the network manager command line interface).

## Connecting to the pi

I usually operate the pi in headless mode and connect via ssh from my computer.
Basically never do I use the pi with a keyboard, mouse, and monitor.

### Static IP

This is bad practice but comes in handy for home computing sometimes.

However, since bookworm, that resulted in flaky, broken pipes
and spotty occurences of key exchange errors.
```
% ssh raspberry_pi_wlan
kex_exchange_identification: read: Connection reset by peer
Connection reset by 192.168.1.93 port 22
```

The actual error shown in the ssh logs on the pi showed
```
getpeername failed: Transport endpoint is not connected
```

Was super weird, so I reverted that back.
Using `raspberrypi.local` works just as good as a static IP.


### SSH config

The entry in the `~/.ssh/config` file for my pi currently looks like this

```
Host pi
	HostName raspberrypi.local
	User <myusername>
	IdentityFile ~/.ssh/id_rsa_raspberry_pi
	ServerAliveInterval 30
	ServerAliveCountMax 5
```

This works reliably.

## Projects

### Wordpress server

Open up a root shell via `sudo su -`.

Update packages
```
$ apt-get update
$ apt-get upgrade
```

#### Apache

Install Apache and check status
```
$ apt install apache2
$ systemctl status apache2
```
If you navigate to http://raspberrypi.local, you see the Debian Apache
default page.

#### MariaDB for SQL

Next install MariaDB (as a replacement for the mysql server) and check
its status.
```
$ apt install mariadb-server
$ apt install mariadb-client
$ systemctl status mariadb
```

Start security script
```
$ mysql_secure_installation
NOTE: RUNNING ALL PARTS OF THIS SCRIPT IS RECOMMENDED FOR ALL MariaDB
      SERVERS IN PRODUCTION USE!  PLEASE READ EACH STEP CAREFULLY!

In order to log into MariaDB to secure it, we'll need the current
password for the root user. If you've just installed MariaDB, and
haven't set the root password yet, you should just press enter here.

Enter current password for root (enter for none):

# This is *not* the system root. This is the MySQL root.
# I had trouble with special characters in the password, so I created
# a secure password containing letters, capital letters, and numbers.

OK, successfully used password, moving on...

Setting the root password or using the unix_socket ensures that nobody
can log into the MariaDB root user without the proper authorisation.

You already have your root account protected, so you can safely answer 'n'.

Switch to unix_socket authentication [Y/n]

# I selected 'n'

Change the root password? [Y/n]

Change the root password? [Y/n] Y

# Just re-enter the MySQL root password here again.
# This time it double checks the password.

New password: 
Re-enter new password: 
Password updated successfully!
Reloading privilege tables..
 ... Success!


By default, a MariaDB installation has an anonymous user, allowing anyone
to log into MariaDB without having to have a user account created for
them.  This is intended only for testing, and to make the installation
go a bit smoother.  You should remove them before moving into a
production environment.

Remove anonymous users? [Y/n] Y
 ... Success!

Normally, root should only be allowed to connect from 'localhost'.  This
ensures that someone cannot guess at the root password from the network.

Disallow root login remotely? [Y/n] Y
 ... Success!

By default, MariaDB comes with a database named 'test' that anyone can
access.  This is also intended only for testing, and should be removed
before moving into a production environment.

Remove test database and access to it? [Y/n] Y
 - Dropping test database...
 ... Success!
 - Removing privileges on test database...
 ... Success!

Reloading the privilege tables will ensure that all changes made so far
will take effect immediately.

Reload privilege tables now? [Y/n] Y
 ... Success!

Cleaning up...

All done!  If you've completed all of the above steps, your MariaDB
installation should now be secure.

Thanks for using MariaDB!
```

Next we create a user for MariaDB.
Still in a root shell, enter the following.
```
$ mysql
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 39
Server version: 10.11.6-MariaDB-0+deb12u1 Debian 12

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> CREATE DATABASE wordpress_amber_maria_db;
Query OK, 1 row affected (0.001 sec)

MariaDB [(none)]> CREATE USER 'wordpress_amber_user'@'%' IDENTIFIED BY 'enter_a_password_here';
Query OK, 0 rows affected (0.003 sec)

MariaDB [(none)]> GRANT ALL ON wordpress_amber_maria_db.* TO 'wordpress_amber_user'@'%';
Query OK, 0 rows affected (0.003 sec)

MariaDB [(none)]> exit
Bye
```


### Interface connecting the pi to a Cortex M4

Used for a lab where students are supposed to have an easy way of interfacing a TI Cortex M4 (Tiva)
without installing the entire toolchain on their own computers.

Done before bringing this repo to life -- to be updated here at some point when I re-do it.

### Raspberry Camera

I use an IMX219 module.
