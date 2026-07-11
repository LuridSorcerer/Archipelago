from BaseClasses import Location
from dataclasses import dataclass, field
import json
from pathlib import Path


DATA_PATH = Path(__file__).parent / "data" / "locations.json"
LOCATION_ID_BASE = 900000


@dataclass
class LocationData:
    id: int
    name: str
    region: str
    category: list[str]
    requires: [str]
    victory: bool = False
    place_item_category: list[str] = field(default_factory=list)


class LoMLocation(Location):
    game = "Legend of Mana"


with open(DATA_PATH, encoding="utf-8") as f:
    raw_locations = json.load(f)


location_data = {}


# Build lookup table
for index, entry in enumerate(raw_locations['data']):
    location = LocationData(
        id=LOCATION_ID_BASE + index,
        name=entry['name'],
        region="Home",
        category= entry.get('category',[]),
        requires=entry.get('requires',""),
        victory=entry.get('victory',False),
        place_item_category=entry.get("place_item_category",[]),
    )
    location_data[location.name] = location