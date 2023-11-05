#!/bin/bash

cat series.json | jq -rc ' {title: .title, total_books: [(.works[] | .books_count | tonumber)] | add }' | 
jq -s 'sort_by(-.total_books) | .[0:5][] | .title'

