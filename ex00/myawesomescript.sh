#!/usr/bin/env bash

input_url=$1

output=$(\curl -sI "$input_url" | grep -i "location:" | cut -d ' ' -f 2)

printf "%s\n" "$output"