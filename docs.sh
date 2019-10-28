#!/bin/bash

BASE=$(readlink -f $0)
BASE_DIR=$(dirname "$BASE")

# Colors and customization
BACKGROUND='#c93648'
FOREGROUND=''
FONT='mononoki:12'
PROMPT='Select: '


# Default Browser to open the docs
BROWSER='firefox'


python $BASE_DIR/devdocs.py laravel:$1 | \
    dmenu -i -l 20 \
    -fn $FONT \
    -sb $BACKGROUND \
    -p $PROMPT | \
    xargs -I {} $BROWSER {}
