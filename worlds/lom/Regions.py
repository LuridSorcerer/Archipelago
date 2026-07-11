from BaseClasses import Region

from .Locations import LoMLocation, location_data


def create_regions(world):

    menu = Region(
        "Menu",
        world.player,
        world.multiworld
    )

    home = Region(
        "Home",
        world.player,
        world.multiworld
    )

    menu.connect(home)

    home.locations.append(
        LoMLocation(
            world.player,
            "Home #1",
            world.location_name_to_id["Home #1"],
            home
        )
    )

    world.multiworld.regions += [
        menu,
        home
    ]