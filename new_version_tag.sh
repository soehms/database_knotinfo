#!/bin/bash
# This script is used by GitHub Action .github/workflows/check_version_changed.yml
# It checks if create_knotinfo_csv.py did find new content in the databases.
# In that case the changes are commited and a new version tag is created.
# Please don't use this scrip for other purpose!
GIT_DIFF=`git diff`
DAY=$(date +%-d)
MONTH=$(date +%-m)
YEAR=$(date +%Y)
TAG=$YEAR"."$MONTH"."$DAY

git config user.email "seb.oehms@gmail.com"
git config user.name "Sebastian Oehms"

if [ -n "$GIT_DIFF" ]
then
    COMMIT_MSG="automatic upgrade to version "$TAG" on "$(date +%F)
    echo "value = '"$TAG"'" > database_knotinfo/__version__.py
    git commit -m "$COMMIT_MSG" .
    echo "New version "$TAG" commited"
    git push
    echo "New database content pushed to repository"
    git tag -a -m "$COMMIT_MSG" $TAG
    echo "New tag "$TAG" created"
    git push --tags
    echo "New version "$TAG" pushed to repository"
else
    # Make a dummy commit to keep the scheduled workflow alive
    # https://stackoverflow.com/questions/67184368/prevent-scheduled-github-actions-from-becoming-disabled
    echo  "Version " $TAG "omitted!" >> keep_schedule_alive.txt
    COMMIT_MSG="omitting version "$TAG" on "$(date +%F)
    git commit -m "$COMMIT_MSG" .
    echo "No differences found"
    git push
fi
