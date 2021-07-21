#!/bin/bash
# This script is used by GitHub Action .github/workflows/check_version_changed.yml
# It checks if a new version tag has been created on tat day
# and returns it as a result
# Please don't use this scrip for other purpose!
DATE=$(date +%F)
TAG_LONG=`git tag -n1 --points-at HEAD | grep $DATE`
if [ "$TAG_LONG" != "" ]
then
    TAG_ARR=($TAG_LONG)
    echo ${TAG_ARR[0]}
fi
