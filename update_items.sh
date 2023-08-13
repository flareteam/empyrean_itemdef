#!/bin/bash

SCRIPT_PATH="$(dirname "$0")/main.py"
FLARE_GAME_PATH="$1"

if [ ! -d "$FLARE_GAME_PATH" ]; then
    echo "Error: Path does not exist."
    exit 1
fi

ITEM_PATH="$FLARE_GAME_PATH/mods/empyrean_campaign/items/categories"

if [ ! -d "$ITEM_PATH" ]; then
    echo "Error: Path does appear to contain Flare Empyrean data."
    exit 2
fi

python $SCRIPT_PATH  1  4 > "$ITEM_PATH/level_1.txt"
python $SCRIPT_PATH  2  12 > "$ITEM_PATH/level_2.txt"
python $SCRIPT_PATH  3  38 > "$ITEM_PATH/level_3.txt"
python $SCRIPT_PATH  4  64 > "$ITEM_PATH/level_4.txt"
python $SCRIPT_PATH  5  96 > "$ITEM_PATH/level_5.txt"
python $SCRIPT_PATH  6 110 > "$ITEM_PATH/level_6.txt"
python $SCRIPT_PATH  7 139 > "$ITEM_PATH/level_7.txt"
python $SCRIPT_PATH  8 168 > "$ITEM_PATH/level_8.txt"
python $SCRIPT_PATH  9 204 > "$ITEM_PATH/level_9.txt"
python $SCRIPT_PATH 10 218 > "$ITEM_PATH/level_10.txt"
python $SCRIPT_PATH 11 247 > "$ITEM_PATH/level_11.txt"
python $SCRIPT_PATH 12 276 > "$ITEM_PATH/level_12.txt"
python $SCRIPT_PATH 13 311 > "$ITEM_PATH/level_13.txt"
python $SCRIPT_PATH 14 325 > "$ITEM_PATH/level_14.txt"
python $SCRIPT_PATH 15 354 > "$ITEM_PATH/level_15.txt"
python $SCRIPT_PATH 16 383 > "$ITEM_PATH/level_16.txt"
