#!/bin/bash
result=$(ps -ef | grep autoCommit.sh)

echo $result

IFS=' ' eval 'array=($result)'

condition1="${array[7]}"
condition2="${array[8]}"

if [ $condition1 = "sh" ] && [ $condition2 = "autoCommit.sh" ]
then
  pid=${array[1]}

  kill "$pid"
fi
