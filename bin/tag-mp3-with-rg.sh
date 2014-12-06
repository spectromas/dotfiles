#!/bin/bash
# Error codes
ARGUMENT_NOT_DIRECTORY=10
FILE_NOT_FOUND=11
# Check that the argument passed to this script is a directory.
# If it's not, then exit with an error code.
if [ ! -d "$1" ]
then
    echo -e "33[1;37mArg "$1" is NOT a directory!33[0m"
    exit $ARGUMENT_NOT_DIRECTORY
fi
# Count the number of mp3 files in this directory.
mp3num=`ls "$1" | grep -c \\.mp3`
# If no mp3 files are found in this directory,
# then exit without error.
if [ $mp3num -lt 1 ]
then
    echo -e "33[1;33m"$1" 33[1;37m--> (No mp3 files found)33[0m"
    exit 0
else
    echo -e "33[1;36m"$1" 33[1;37m--> (33[1;32m"$mp3num"33[1;37m mp3 files)33[0m"
fi
# Run mp3gain on the mp3 files in this directory.
echo -e ""
echo -e "33[1;37mForcing (re)calculation of Replay Gain values for mp3 files and adding them as ID3 tags into the mp3 file...33[0m"
echo -e ""
mp3gain -s i "$1"/*.mp3
echo -e ""
echo -e "33[1;37mDone.33[0m"
echo -e ""
echo -e "33[1;37mAdding ID3 tags with the same calculated info from above...33[0m"
echo -e ""
echo -e ""
echo -e "33[1;37mDone.33[0m"
echo -e ""
echo -e "33[1;37mReplay gain tags successfully added recursively.33[0m"
echo -e ""
