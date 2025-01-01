"""Test the CityBus config flow."""

from collections.abc import Generator
from unittest.mock import MagicMock, patch

import pytest

from homeassistant import config_entries, setup
from homeassistant.components.citybus.const import (
    CONF_DIRECTION,
    CONF_ROUTE,
    CONF_STOP,
    DOMAIN,
)
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResultType


@pytest.fixture
def mock_setup_entry() -> Generator[MagicMock]:
    """Create a mock for the CityBus component setup."""
    with patch(
        "homeassistant.components.citybus.async_setup_entry",
        return_value=True,
    ) as mock_setup_entry:
        yield mock_setup_entry


@pytest.fixture
def mock_citybussin() -> Generator[MagicMock]:
    """Create a mock citybussin module."""
    with patch("homeassistant.components.citybus.config_flow.Citybussin") as citybussin:
        yield citybussin


async def test_user_config(
    hass: HomeAssistant, mock_setup_entry: MagicMock, mock_citybus_lists: MagicMock
) -> None:
    """Test we get the form."""
    await setup.async_setup_component(hass, "persistent_notification", {})
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result.get("type") is FlowResultType.FORM
    assert result.get("step_id") == "route"

    # Select route
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {
            CONF_ROUTE: "4B",
        },
    )
    await hass.async_block_till_done()

    assert result.get("type") is FlowResultType.FORM
    assert result.get("step_id") == "direction"

    # Select direction
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {
            CONF_DIRECTION: "to Campus & CityBus Center",
        },
    )
    await hass.async_block_till_done()

    assert result.get("type") is FlowResultType.FORM
    assert result.get("step_id") == "stop"

    # Select stop
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {
            CONF_STOP: "BUS403",
        },
    )
    await hass.async_block_till_done()

    assert result.get("type") is FlowResultType.CREATE_ENTRY
    assert result.get("data") == {
        "route": "4B",
        "direction": "to Campus & CityBus Center",
        "stop": "BUS403",
    }

    assert len(mock_setup_entry.mock_calls) == 1
