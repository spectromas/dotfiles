#!/bin/bash
cd ~/Downloads/Torrents/watch/ || exit    # set your watch directory here
[[ "$1" =~ xt=urn:btih:([^&amp;/]+) ]] || exit;
echo "d10:magnet-uri${#1}:${1}e" > "meta-${BASH_REMATCH[1]}.torrent"