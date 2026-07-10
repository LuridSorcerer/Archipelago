from BaseClasses import Item, Location, Region, ItemClassification
from worlds.AutoWorld import World
from .Options import LoMOptions

class LoMItem(Item):
    game = "Legend of Mana"


class LoMLocation(Location):
    game = "Legend of Mana"


class LegendOfManaWorld(World):
    """
    Legend of Mana
    """

    game = "Legend of Mana"

    options_dataclass = LoMOptions

    item_name_to_id = {
        "Jade Egg": 1,
    }

    location_name_to_id = {
        "Mailbox": 1,
    }

    def create_regions(self):

        menu = Region(
            "Menu",
            self.player,
            self.multiworld
        )

        home = Region(
            "Home",
            self.player,
            self.multiworld
        )

        menu.connect(home)

        home.locations.append(
            LoMLocation(
                self.player,
                "Mailbox",
                self.location_name_to_id["Mailbox"],
                home
            )
        )

        self.multiworld.regions += [
            menu,
            home
        ]

    def create_items(self):
        self.multiworld.itempool.append(
            LoMItem(
                "Jade Egg",
                ItemClassification.progression,
                self.item_name_to_id["Jade Egg"],
                self.player
            )
        )
    
    def set_rules(self):
        self.multiworld.completion_condition[self.player] = \
            lambda state: state.has(
                "Jade Egg",
                self.player
            )
