# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import Item, GildedRose

if __name__ == "__main__":
    print ("OMGHAI!")
    sulfuras="Sulfuras, Hand of Ragnaros"
    backstage="backstage passes to a TAFKAL80ETC concert"
    items = [
             Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
             Item(name="Aged Brie", sell_in=2, quality=0),
             Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
             Item(name=sulfuras, sell_in=0, quality=80),
             Item(name=sulfuras, sell_in=-1, quality=80),
             Item(name=backstage, sell_in=15, quality=20),
             Item(name=backstage, sell_in=10, quality=49),
             Item(name=backstage, sell_in=5, quality=49),
             Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            ]

    days = 2
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()
