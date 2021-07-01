#!/bin/bash
# This script is used by GitHub Action .github/workflows/check_version_changed.yml
# It checks if a new version tag has been created on tat day
# and returns it as a result
# Please don't use this scrip for other purpose!
MONTH=$(date +%m)
YEAR=$(date +%g)
COMMIT_MSG="automatic upgrade to version "$TAG" on "$(date +%F)
TAG=$YEAR"."$MONTH
DAY=$(date +%F)
TAG_LONG=`git tag -n1 --points-at HEAD | grep $DAY`
if [ "$TAG_LONG" != "" ]
then
    echo "$TAG"
fi
