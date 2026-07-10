from BaseClasses import Item, ItemClassification


class LoMItem(Item):
    game = "Legend of Mana"


item_table = {
    "Jade Egg": ItemClassification.progression,
}