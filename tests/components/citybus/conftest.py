"""Test helpers for CityBus tests."""

from collections.abc import Generator
from unittest.mock import MagicMock, patch

import pytest

from .const import BASIC_RESULTS


@pytest.fixture
def mock_citybus_lists(mock_citybus: MagicMock) -> MagicMock:
    """Mock all list functions in citybus to test validate logic."""
    instance = mock_citybus.return_value

    instance._get_routes.return_value = []

    instance.get_bus_routes.return_value = [
        {
            "key": "49c4b590-376d-40f9-afdc-9d75023719c8",
            "name": "Lindberg Express",
            "shortName": "35E",
            "directionList": [
                {
                    "direction": {
                        "key": "3ccc7392-d505-48aa-8501-73779d43a2c3",
                        "name": "Village West and Cottage Apts Loop",
                    },
                    "destination": "Village West/Cottage Apts to/from Purdue",
                    "patternList": [
                        {
                            "key": "f0010f83-7c44-4e8d-b01d-b0e119e5666e",
                        }
                    ],
                    "serviceInterruptionKeys": [],
                }
            ],
        },
        {
            "key": "7c063399-7c5e-4a41-982b-2b2dc3d33b00",
            "name": "Purdue West",
            "shortName": "4B",
            "directionList": [
                {
                    "direction": {
                        "key": "41513758-37f3-44f9-b82e-895b9147299d",
                        "name": "to CityBus Center",
                    },
                    "destination": "to Campus & CityBus Center",
                    "patternList": [
                        {
                            "key": "52e9e779-714c-43db-ac60-0d404d1a34ba",
                            "isDisplay": True,
                        }
                    ],
                    "serviceInterruptionKeys": [],
                },
                {
                    "direction": {
                        "key": "6ead834f-df69-4330-93c4-79b7582423cb",
                        "name": "to WL Walmart",
                    },
                    "destination": "to Campus & WL Walmart",
                    "patternList": [
                        {
                            "key": "3328c98f-ae0b-4319-be6c-bf03d7bf056c",
                            "isDisplay": True,
                        }
                    ],
                    "serviceInterruptionKeys": [],
                },
            ],
        },
    ]

    return instance


@pytest.fixture
def mock_citybus() -> Generator[MagicMock]:
    """Create a mock citybussin module."""
    with patch("homeassistant.components.citybus.coordinator.Citybussin") as citybussin:
        yield citybussin


@pytest.fixture
def mock_citybus_depart_times(
    mock_citybus: MagicMock,
) -> Generator[MagicMock]:
    """Create a mock of Citybussin depart times."""
    instance = mock_citybus.return_value
    instance.get_next_depart_times.return_value = BASIC_RESULTS

    return instance.get_next_depart_times
