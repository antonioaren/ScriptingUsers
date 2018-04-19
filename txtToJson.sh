#!/usr/bin/env bash

FOLDERS=(/tmp/users/*)

for folders in "${FOLDERS[@]}"
do
    cat ${folders}/*.txt

done