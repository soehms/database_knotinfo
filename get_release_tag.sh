#!/bin/bash
# This script is used by GitHub Action .github/workflows/check_version_changed.yml
# It checks if a new version tag has been created on tat day
# and returns it as a result
# Please don't use this scrip for other purpose!
DAY=$(date +%d)
MONTH=$(date +%m)
YEAR=$(date +%g)
TAG=$YEAR"."$MONTH"."$DAY
DATE=$(date +%F)
TAG_LONG=`git tag -n1 --points-at HEAD | grep $DATE`
if [ "$TAG_LONG" != "" ]
then
    echo "$TAG"
fi
