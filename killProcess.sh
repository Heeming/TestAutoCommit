#!/bin/bash
result=$(ps ax | grep autoCommit.sh)

echo $result

pkill -f "sh autoCommit.sh"