#!/bin/sh
#Arg 1: Old Email
#Arg 2: New Name
#Arg 3: New Email

FILTER_BRANCH_SQUELCH_WARNING=1 git filter-branch -f --env-filter '
OLD_EMAIL="'"${1}"'"
CORRECT_NAME="'"${2}"'"
CORRECT_EMAIL="'"${3}"'"
if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_COMMITTER_NAME="$CORRECT_NAME"
    export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_AUTHOR_NAME="$CORRECT_NAME"
    export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags