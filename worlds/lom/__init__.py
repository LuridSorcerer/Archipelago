from BaseClasses import ItemClassification
from worlds.AutoWorld import World

from .Options import LoMOptions
from .Items import LoMItem, item_table
from .Locations import location_table
from .Regions import create_regions


class LegendOfManaWorld(World):
    """
    Legend of Mana
    """

    game = "Legend of Mana"

    options_dataclass = LoMOptions

    item_name_to_id = {
        "Jade Egg": 1,
    }

    location_name_to_id = location_table

    def create_regions(self):
        create_regions(self)

    def create_items(self):
        for item_name, classification in item_table.items():
            self.multiworld.itempool.append(
                LoMItem(
                    item_name,
                    classification,
                    self.item_name_to_id[item_name],
                    self.player
                )
            )
    
    def set_rules(self):
        self.multiworld.completion_condition[self.player] = \
            lambda state: state.has(
                "Jade Egg",
                self.player
            )
