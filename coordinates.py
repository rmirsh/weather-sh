from dataclasses import dataclass
from typing import List
from urllib.request import urlopen 
import json 

import config 
from exceptions import CantGetCoordinates


@dataclass(slots=True, frozen=True)
class Coordinates():
    latitude: float
    longitude: float


def get_gps_coordinates() -> Coordinates:
    """Returns current coordinates using IP-adress"""
    coordinates = _float_coordinates(_get_coordinates())
    return _round_coordinates(coordinates)


def _float_coordinates(coords) -> Coordinates:
    coords = _get_coordinates()
    lat, lon = map(float, coords)

    return Coordinates(latitude=lat, longitude=lon)
    
    
def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not config.USE_ROUNDED_COORDS:
        return coordinates
    return Coordinates(*map(
        lambda c: round(c, 5),
        [coordinates.latitude, coordinates.longitude]
        ))   

    
def _get_coordinates() -> List:
    try:
        data = json.load(urlopen("http://ipinfo.io/json"))
    except: 
        raise CantGetCoordinates 
    
    coords = data['loc'].split(',')

    return coords 


if __name__ == "__main__":
    print(get_gps_coordinates())
