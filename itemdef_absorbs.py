#!/usr/bin/env python

from itemdef_itemtype import ItemType

absorbs = []
# (min, max, initial_level)
absorbs.insert(ItemType.MELEE_HEAD, (2,2,5))
absorbs.insert(ItemType.RANGED_HEAD, (1,2,5))
absorbs.insert(ItemType.MENT_HEAD, (1,1,5))
absorbs.insert(ItemType.MELEE_CHEST, (1,2,2))
absorbs.insert(ItemType.RANGED_CHEST, (1,1,2))
absorbs.insert(ItemType.MENT_CHEST, (0,1,2))
absorbs.insert(ItemType.MELEE_LEGS, (1,1,2))
absorbs.insert(ItemType.RANGED_LEGS, (0,1,2))
absorbs.insert(ItemType.MENT_LEGS, (0,1,3))
absorbs.insert(ItemType.MELEE_FEET, (0,1,2))
absorbs.insert(ItemType.RANGED_FEET, (0,1,3))
absorbs.insert(ItemType.MENT_FEET, (0,1,4))
absorbs.insert(ItemType.MELEE_HANDS, (0,1,2))
absorbs.insert(ItemType.RANGED_HANDS, (0,1,3))
absorbs.insert(ItemType.MENT_HANDS, (0,1,4))
absorbs.insert(ItemType.MELEE_ARTIFACT, (0,0,0))
absorbs.insert(ItemType.RANGED_ARTIFACT, (0,0,0))
absorbs.insert(ItemType.MENT_ARTIFACT, (0,0,0))
absorbs.insert(ItemType.MELEE_WEAPON, (0,0,0))
absorbs.insert(ItemType.RANGED_WEAPON, (0,0,0))
absorbs.insert(ItemType.MENT_WEAPON, (0,0,0))
absorbs.insert(ItemType.SHIELD, (0,1,1))
# no absorb on rings

