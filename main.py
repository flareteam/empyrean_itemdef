#!/usr/bin/env python

import sys,math
import argparse

from itemdef_itemtype import ItemType
from itemdef_suffix import *
from itemdef_includes import *
from itemdef_prices import *
from itemdef_absorbs import *
from itemdef_requires import *
from itemdef_bonus import *

prefix_melee = ["Fighting", "Warrior", "Warlord"]
prefix_ranged = ["Recon", "Ranger", "Sniper"]
prefix_ment = ["Sorcerer", "Wizard", "Archwizard"]
prefix_shield = ["Keeper", "Paladin", "Templar"]
prefix_rings = ["Wandering", "Adventurer", "Master"]
qualities = ["high", "epic", "rare"]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("item_level", help="The level for this set of items", type=int)
    parser.add_argument("start_id", help="The item id to begin counting from", type=int)
    args = parser.parse_args()

    id = args.start_id
    level = args.item_level
    reorder_pass = False

    sys.stdout.write("# equipment intended for players level " + str(level) + "\n\n")

    i = ItemType.MELEE_HEAD
    while i < len(ItemType):
        item_class = i % 3
        item_tier = int(math.floor((level-1)/4))
        item_subtier = (level-1) % 4

        # When creating base-tier items, we want to group the armors together by material type
        # For example, all Leather items should be sequential, followed by all Wool items
        if (item_subtier == 0):
            if (i < ItemType.MELEE_ARTIFACT):
                if (reorder_pass == False and i % 3 == 2):
                    i += 1
                    continue
                elif (reorder_pass == True and i % 3 != 2):
                    i += 1
                    continue
            else:
                if (reorder_pass == False and i == ItemType.MELEE_ARTIFACT):
                    i = ItemType.MELEE_HEAD
                    reorder_pass = True
                    i += 1
                    continue
                else:
                    reorder_pass = False

        # No head-gear for tier 1
        if (level <= 4 and i < 3):
            i += 1
            continue

        if (item_subtier == 0):
            # No belts for subtier 1
            if (i >= ItemType.MELEE_ARTIFACT and i <= ItemType.MENT_ARTIFACT):
                i += 1
                continue

            # use ranger gear subtier 1 below level 4
            # also include mage gear from level 4 on
            if (item_class != 1 and i <= ItemType.MENT_ARTIFACT and level < 4):
                i += 1
                continue
            elif (item_class == 0 and i <= ItemType.MENT_ARTIFACT and level >= 4):
                i += 1
                continue

            # don't include rings
            if (i >= ItemType.FIRE_RING):
                i += 1
                continue

        ## Header
        sys.stdout.write("[item]\n")
        sys.stdout.write("id=" + str(id) + "\n")
        id += 1

        ## Item Name
        sys.stdout.write("name=")
        if (item_subtier > 0):
            if (i >= ItemType.FIRE_RING):
                sys.stdout.write(prefix_rings[item_subtier-1])
            elif (i == ItemType.SHIELD):
                sys.stdout.write(prefix_shield[item_subtier-1])
            elif (i >= ItemType.MELEE_ARTIFACT and i <= ItemType.MENT_ARTIFACT):
                # artifacts also use ring prefixes
                sys.stdout.write(prefix_rings[item_subtier-1])
            elif (item_class == 0):
                sys.stdout.write(prefix_melee[item_subtier-1])
            elif (item_class == 1):
                sys.stdout.write(prefix_ranged[item_subtier-1])
            elif (item_class == 2):
                sys.stdout.write(prefix_ment[item_subtier-1])

            sys.stdout.write(" ");

        if (item_tier == 0):
            sys.stdout.write(suffix1[i])
        elif (item_tier == 1):
            sys.stdout.write(suffix2[i])
        elif (item_tier == 2):
            sys.stdout.write(suffix3[i])
        elif (item_tier == 3):
            sys.stdout.write(suffix4[i])

        sys.stdout.write("\n")

        ## Base item include path
        sys.stdout.write("INCLUDE items/base/")

        if (item_tier == 0):
            sys.stdout.write(includes1[i])
        elif (item_tier == 1):
            sys.stdout.write(includes2[i])
        elif (item_tier == 2):
            sys.stdout.write(includes3[i])
        elif (item_tier == 3):
            sys.stdout.write(includes4[i])

        sys.stdout.write("\n")

        ## Level
        sys.stdout.write("level=" + str(level) + "\n")

        ## Quality
        if (item_subtier > 0):
            sys.stdout.write("quality=" + qualities[item_subtier-1] + "\n")

        ## Price
        sys.stdout.write("price=" + str(prices[i] * level) + "\n")

        ## Weapon Damage
        if (i >= ItemType.MELEE_WEAPON and i <= ItemType.MENT_WEAPON):
            # 5 bonus per level = 20 base per item tier
            dmgmin = 25 + (20 * item_tier)
            dmgmax = 30 + (20 * item_tier)

            if (i == ItemType.MELEE_WEAPON):
                sys.stdout.write("dmg=melee,")
            elif (i == ItemType.RANGED_WEAPON):
                sys.stdout.write("dmg=ranged,")
            elif (i == ItemType.MENT_WEAPON):
                sys.stdout.write("dmg=ment,")
            
            sys.stdout.write(str(dmgmin) + "," + str(dmgmax) + "\n")

        ## Armor absorption
        if ((i < ItemType.MELEE_WEAPON or i == ItemType.SHIELD) and level >= absorbs[i][2] and absorbs[i][2] != 0):
            absmin = absorbs[i][0]
            absmax = absorbs[i][1]
            abslvl = absorbs[i][2]

            if (absmin == absmax):
                absmin += int(math.floor(((level-abslvl)/2)))
                if (i == ItemType.SHIELD):
                    absmin += (item_tier * 3)
                absmax = absmin
                if ((level-abslvl) % 2 != 0):
                    absmax += 1
            else:
                absmin +=int(math.floor(((level-abslvl)/2)+0.5))
                if (i == ItemType.SHIELD):
                    absmin += (item_tier * 3)
                absmax = absmin
                if ((level-abslvl) % 2 == 0):
                    absmax += 1

            sys.stdout.write("abs=" + str(absmin))
            if (absmin != absmax):
                sys.stdout.write("," + str(absmax))

            sys.stdout.write("\n")

        ## Base stat requirements
        # Level 1 weapons have the same stat requirements of their level 2 counterparts
        if (level == 1 and i >= ItemType.MELEE_WEAPON and i <= ItemType.MENT_WEAPON):
            sys.stdout.write("requires_stat=" + requires1[i][0] + "," + str(requires1[i][1]) + "\n")

        if (requires1[i][3] != 0 and level >= requires1[i][3]):
            req = requires1[i][1] + (requires1[i][2] * (level-requires1[i][3]))
            sys.stdout.write("requires_stat=" + requires1[i][0] + "," + str(req) + "\n")

        if (requires2[i][3] != 0 and level >= requires2[i][3]):
            if (item_subtier != 0 or (i >= ItemType.MELEE_WEAPON and i <= ItemType.SHIELD)):
                req = requires2[i][1] + (requires2[i][2] * (level-requires2[i][3]))
                sys.stdout.write("requires_stat=" + requires2[i][0] + "," + str(req) + "\n")

        ## Level requirement
        if (requires3[i][2] != 0 and level >= requires3[i][2]):
            req = requires3[i][0] + (requires3[i][1] * (level-requires3[i][2]))
            sys.stdout.write("requires_level=" + str(req) + "\n")

        ## Bonuses
        if (item_subtier != 0 and bonus1[i][2] != 0 and level >= bonus1[i][2]):
            bonus = 0
            bonus_tier = int(math.floor((level-bonus1[i][2])/4))
            if (i >= ItemType.MELEE_WEAPON and i <= ItemType.SHIELD):
                bonus = (bonus1[i][1] * item_subtier) + bonus1[i][3]
            else:
                bonus = (bonus1[i][1] * (level-bonus1[i][2]-bonus_tier+1)) + bonus1[i][3]

            sys.stdout.write("bonus=" + bonus1[i][0] + "," + str(bonus) + "\n")

        if (item_subtier != 0 and bonus2[i][2] != 0 and level >= bonus2[i][2]):
            bonus = 0
            bonus_tier = int(math.floor((level-bonus2[i][2])/4))
            if (i >= ItemType.MELEE_WEAPON and i <= ItemType.SHIELD):
                bonus = (bonus2[i][1] * item_subtier) + bonus2[i][3]
            else:
                bonus = (bonus2[i][1] * (level-bonus2[i][2]-bonus_tier+1)) + bonus2[i][3]

            sys.stdout.write("bonus=" + bonus2[i][0] + "," + str(bonus) + "\n")

        sys.stdout.write("\n")
        i += 1

if __name__ == "__main__":
    main()
