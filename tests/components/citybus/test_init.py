"""The tests for the CityBus sensor component."""

from unittest.mock import MagicMock
from urllib.error import HTTPError

from homeassistant.config_entries import ConfigEntryState
from homeassistant.core import HomeAssistant

from . import assert_setup_sensor
from .const import CONFIG_BASIC


async def test_setup_retry(
    hass: HomeAssistant,
    mock_citybus: MagicMock,
    mock_citybus_lists: MagicMock,
    mock_citybus_estimates: MagicMock,
) -> None:
    """Verify that a list of messages are rendered correctly."""

    mock_citybus_estimates.side_effect = HTTPError(
        "url", 500, "error", MagicMock(), None
    )
    await assert_setup_sensor(
        hass, CONFIG_BASIC, expected_state=ConfigEntryState.SETUP_RETRY
    )
