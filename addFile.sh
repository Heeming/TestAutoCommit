#!/bin/bash
echo "git add file"

if [ "$1" = "" ]
then echo "please write file name which need to git add"
else
  filename="$1"
  git add $filename > /dev/null
  git commit -m "Add file::$filename" > /dev/null
  git push -u origin auto-commit > /dev/null
fi
