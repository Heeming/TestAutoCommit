#!/bin/bash
while :
do
  #echo "Checking for uncommitted changes in the git working tree"

  if ! git diff --quiet
  then
    git checkout auto-commit > /dev/null
    git add . > /dev/null
    git commit -m "Auto Commit" > /dev/null
    git push -u origin auto-commit > /dev/null

  #else
    #echo "Working tree clean. Nothing to commmit."
  fi

  sleep 60
done
