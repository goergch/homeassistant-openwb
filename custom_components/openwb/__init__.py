from homeassistant.config_entries import SOURCE_IMPORT, ConfigEntry

from .const import DOMAIN, DEFAULT_BASE_TOPIC, CHARGE_MODES
from homeassistant.components import mqtt

import voluptuous as vol


SERVICE_SET_CHARGE_MODE = "set_charge_mode"
SERVICE_SET_CHARGE_MODE_TOPIC = "/set/ChargeMode"

SERVICE_SCHEMA_SET_CHARGE_MODE = vol.Schema(
    {
        vol.Required("charge_mode"): str,
    }
)


async def async_setup(hass, config):
    """Set up the OpenWb component."""

    async def set_charge_mode(call):

        chargemode = call.data.get("charge_mode", "")

        mqtt.async_publish(
            hass,
            DEFAULT_BASE_TOPIC + SERVICE_SET_CHARGE_MODE_TOPIC,
            CHARGE_MODES.get(chargemode),
        )
        return

    hass.services.async_register(
        DOMAIN,
        SERVICE_SET_CHARGE_MODE,
        set_charge_mode,
        schema=SERVICE_SCHEMA_SET_CHARGE_MODE,
    )
    return True


async def async_setup_entry(hass, entry):
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "binary_sensor")
    )
    return True