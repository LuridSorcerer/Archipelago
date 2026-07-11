from BaseClasses import ItemClassification
from worlds.AutoWorld import World

from .Options import LoMOptions
from .Items import LoMItem, item_data
from .Locations import location_data
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

    location_name_to_id = {
        name: location.id
        for name, location in location_data.items()
    }

    def create_regions(self):
        create_regions(self)

    def create_items(self):
        for name, data in item_data.items():
            if data["classification"] == "progression":
                classification = ItemClassification.progression
            else:
                classification = ItemClassification.filler

            self.multiworld.itempool.append(
                LoMItem(
                    name,
                    classification,
                    data["id"],
                    self.player
                )
            )
        print(len(self.multiworld.itempool))
    
    def set_rules(self):
        self.multiworld.completion_condition[self.player] = \
            lambda state: state.has(
                "Jade Egg",
                self.player
            )
