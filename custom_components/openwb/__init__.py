
from homeassistant.config_entries import SOURCE_IMPORT, ConfigEntry

from .const import DOMAIN, CONF_OPENWB_ADDRESS


async def async_setup(hass: HomeAssistantType, config: dict):
    """Set up the Tasmota component."""
    return True

