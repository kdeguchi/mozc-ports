# Latest version mozc ports for FreeBSD

The latest version of mozc is available for use on FreeBSD.
Fcitx5 is also supported, so you can get the source code from https://github.com/fcitx/mozc.

I can guarantee that Fcitx5 which I use regularly will work,
but I can't guarantee that the others will work,
only that poudriere will build everything.

You can download these files and overwrite ports tree, or use ports overlays method.
I recommend using ports overlays method.

## ports overlay method

Add in your `/etc/make.conf` as follows:

`OVERLAYS+=/your/download/directory/mozc-ports`
