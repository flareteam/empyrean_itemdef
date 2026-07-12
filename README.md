# Item generation script for Flare's Empyrean mod

This is an offline/auxiliary tool that generates Flare engine item definition files
for the Empyrean campaign mod. It outputs item data to stdout, which can be redirected
into the appropriate mod data files. It is not used at runtime.

The script produces a full set of equipment (armor, weapons, shields, artifacts, and
rings) for a given player level, with stats scaled to that level.

## Usage

```
python main.py item_level start_id
```

### Arguments

| Argument    | Type | Description |
|-------------|------|-------------|
| `item_level` | int  | The player level to generate items for (1–16). Determines item tier, subtier, base material, stat scaling, and bonuses. |
| `start_id`   | int  | The first item ID to assign. Each generated item gets an incrementing ID starting from this value. |

### Example

Generate level 5 items beginning at ID 96:

```
python main.py 5 96
```

The output is a series of Flare-format `[item]` blocks written to stdout.

### Batch generation

A helper script `update_items.sh` is included to regenerate all item levels at once.
It calls `main.py` for each level (1–16) and writes the output into the correct
location under a Flare game data directory:

```
./update_items.sh /path/to/flare-game
```
