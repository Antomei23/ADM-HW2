#!/bin/bash

declare -a sums

while IFS="|" read -r title sum; do
    sums+=("$sum:$title")
done < <(jq -r 'select(.works != null) | .title + "|" + ( (.works | map(.books_count | tonumber) | add) | tostring)' series.json)


IFS=$'\n' sorted=($(sort -t ":" -k 1,1nr <<<"${sums[*]}")); unset IFS
printf "%s\n" "${sorted[@]:0:5}"
