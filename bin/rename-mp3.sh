#!/bin/sh

for FILE in *.mp3
do
    TITLE="$(id3info "$FILE" | grep TIT2 | sed 's/^.*): //g')"
    TRACK="$(id3info "$FILE" | grep TRCK | sed 's/^.*): //g')"
    echo "## Renaming $FILE to $TRACK - ${TITLE}.mp3"
    mv -i "$FILE" "$TRACK. ${TITLE}.mp3"
done
