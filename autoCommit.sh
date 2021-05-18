#!/bin/bash
while :
do
  #echo "Checking for uncommitted changes in the git working tree"

  if ! git diff --quiet
  then
    git --paginate checkout auto-commit
    git --paginate add .
    git --paginate commit -m "Auto Commit"
    git --paginate push -u origin auto-commit

  #else
    #echo "Working tree clean. Nothing to commmit."
  fi

  sleep 60
done
