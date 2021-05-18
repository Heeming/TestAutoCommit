#!/bin/bash
echo "UserCommit and Push"

branch="$1"
message="$2"

git checkout $branch > /dev/null
git merge --squash auto-commit > /dev/null
git commit -m "$message" > /dev/null
git push -u origin master > /dev/null

git checkout -b auto-commit-temp > /dev/null
git merge --no-edit auto-commit > /dev/null

git commit --amend -m "User makes commit and push it to user branch." > /dev/null
git push -f > /dev/null

git branch -d auto-commit > /dev/null
git branch -m auto-commit-temp auto-commit > /dev/null

git push -u origin auto-commit > /dev/null
