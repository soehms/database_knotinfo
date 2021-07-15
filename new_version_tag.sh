#!/bin/bash
# This script is used by GitHub Action .github/workflows/check_version_changed.yml
# It checks if create_knotinfo_csv.py did find new content in the databases.
# In that case the changes are commited and a new version tag is created.
# Please don't use this scrip for other purpose!
GIT_DIFF=`git diff`
if [ -n "$GIT_DIFF" ]
then
    DAY=$(date +%d)
    MONTH=$(date +%m)
    YEAR=$(date +%g)
    TAG=$YEAR"."$MONTH"."$DAY
    COMMIT_MSG="automatic upgrade to version "$TAG" on "$(date +%F)
    echo "value = '"$TAG"'" > database_knotinfo/__version__.py
    git config user.email "seb.oehms@gmail.com"
    git config user.name "Sebastian Oehms"
    git commit -m "$COMMIT_MSG" .
    echo "New version "$TAG" commited"
    git push
    echo "New database content pushed to repository"
    git tag -a -m "$COMMIT_MSG" $TAG
    echo "New tag "$TAG" created"
    git push --tags
    echo "New version "$TAG" pushed to repository"
else
    echo "No differences found"
fi
