# Attention!
Due to changes in the UNIX Domain Socket in FreeBSD 15.0-CURRENT at https://github.com/freebsd/freebsd-src/commit/d15792780760ef94647af9b377b5f0a80e1826bc, mozc does not work well.

If you are using 15.0-CURRENT, I would recommend updating to https://github.com/freebsd/freebsd-src/commit/6ac71c4a52348fc2e47d7d4a5c06c5ffc45660f3 or lator.
It seems that mozc works well.

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

If you use poudriere, you may need to add to `/etc/make.conf` as follows:

    .ifndef POUDRIERE_BUILD_TYPE
    OVERLAYS+=/your/download/directory/mozc-ports
    .endif
