# -*- coding: utf-8 -*-
import math
class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def menor_cero_sell_in(self,item,sulfuras):
        if item.sell_in < 0:
            if item.name != "Aged Brie":
                if item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if item.quality > 0 and item.name != sulfuras:
                        item.quality = item.quality - 1
                else:#item.name == "Backstage passes to a TAFKAL80ETC concert":
                    pivote=item.quality
                    item.quality = item.quality - pivote
            elif item.quality < 50: #item.name == "Aged Brie":
                item.quality = item.quality + 1
            

    def update_quality(self):
        for item in self.items:
            back="Backstage passes to a TAFKAL80ETC concert"
            sulfuras="Sulfuras, Hand of Ragnaros"
            if item.name != "Aged Brie" and item.name != back and  item.quality > 0 and item.name != sulfuras:
                item.quality = item.quality - 1
            elif item.quality < 50 and item.name == back:
                if item.sell_in < 11 or item.sell_in < 6:
                    item.quality = item.quality + 1
                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            self.menor_cero_sell_in(item,sulfuras)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
