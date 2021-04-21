class GildedRose(object):

    BRIE = "Aged Brie"
    CONCERT = "Backstage passes to a TAFKAL80ETC concert"
    SULFARAS = "Sulfuras, Hand of Ragnaros"

    def __init__(self, items):
        self.items = items

    def increase_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1

    def not_sulfaras(self, item):
        if item.quality > 0:
            if item.name != GildedRose.SULFARAS:
                item.quality = item.quality - 1

    def update_quality(self):
        for item in self.items:
            if item.name != GildedRose.BRIE and item.name != GildedRose.CONCERT:
                self.not_sulfaras(item)
            else:
                self.increase_quality(item)
                if item.name == GildedRose.CONCERT:
                    if item.sell_in < 11:
                        self.increase_quality(item)
                    if item.sell_in < 6:
                        self.increase_quality(item)
            if item.name != GildedRose.SULFARAS:
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != GildedRose.BRIE:
                    if item.name != GildedRose.CONCERT:
                        self.not_sulfaras(item)
                    else:
                        item.quality = 0
                else:
                    self.increase_quality(item)
