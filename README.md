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

Done before bringing this repo to life -- to be updated here at some point when I re-do it.

### Interface connecting the pi to a Cortex M4

Used for a lab where students are supposed to have an easy way of interfacing a TI Cortex M4 (Tiva)
without installing the entire toolchain on their own computers.

Done before bringing this repo to life -- to be updated here at some point when I re-do it.

### Raspberry Camera

I use an IMX219 module.
