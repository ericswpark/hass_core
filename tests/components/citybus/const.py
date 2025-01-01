"""Constants for CityBus tests."""

from homeassistant.components.citybus.const import (
    CONF_DIRECTION,
    CONF_ROUTE,
    CONF_STOP,
    DOMAIN,
)
from homeassistant.components.sensor import DOMAIN as SENSOR_DOMAIN

VALID_ROUTE = "4B"
VALID_DIRECTION = "to Campus & CityBus Center"
VALID_STOP = "BUS403"
VALID_COORDINATOR_KEY = f"{VALID_ROUTE}-{VALID_DIRECTION}-{VALID_STOP}"
VALID_STOP_TITLE = "Walmart West Lafayette (at Shelter)"
SENSOR_ID = (
    "sensor.4b_to_campus_citybus_center_walmart_west_lafayette_at_shelter_bus403"
)

ROUTE_2 = "35E"
DIRECTION_2 = "Village West/Cottage Apts to/from Purdue"
STOP_2 = "BUS567"

SENSOR_ID_2 = "sensor.35e_village_west_cottage_apts_to_from_purdue_ford_hall_on_stadium_ave_bus567"

PLATFORM_CONFIG = {
    SENSOR_DOMAIN: {
        "platform": DOMAIN,
        CONF_ROUTE: VALID_ROUTE,
        CONF_DIRECTION: VALID_DIRECTION,
        CONF_STOP: VALID_STOP,
    },
}


CONFIG_BASIC = {
    DOMAIN: {
        CONF_ROUTE: VALID_ROUTE,
        CONF_DIRECTION: VALID_DIRECTION,
        CONF_STOP: VALID_STOP,
    }
}

CONFIG_BASIC_2 = {
    DOMAIN: {
        CONF_ROUTE: ROUTE_2,
        CONF_DIRECTION: DIRECTION_2,
        CONF_STOP: STOP_2,
    }
}

BASIC_RESULTS = [
    {
        "route": {
            "title": VALID_ROUTE,
            "id": VALID_ROUTE,
        },
        "stop": {
            "name": VALID_STOP_TITLE,
            "id": VALID_STOP,
        },
        "estimatedDepartTimeUtc": "2024-10-26T00:29:00Z",
    },
    {
        "route": {
            "title": ROUTE_2,
            "id": ROUTE_2,
        },
        "stop": {
            "name": VALID_STOP_TITLE,
            "id": VALID_STOP,
        },
        "estimatedDepartTimeUtc": "2024-10-28T00:29:00Z",
    },
]

NO_UPCOMING = [
    {
        "route": {
            "title": VALID_ROUTE,
            "id": VALID_ROUTE,
        },
        "stop": {
            "name": VALID_STOP_TITLE,
            "id": VALID_STOP,
        },
        "values": [],
    },
    {
        "route": {
            "title": ROUTE_2,
            "id": ROUTE_2,
        },
        "stop": {
            "name": VALID_STOP_TITLE,
            "id": VALID_STOP,
        },
        "values": [],
    },
]
