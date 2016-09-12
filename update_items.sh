#!/bin/bash

SCRIPT_PATH="/home/justin/Projects/empyrean_itemdef/main.py"
ITEM_PATH="/home/justin/Projects/flare-game/mods/empyrean_campaign/items/categories"

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
