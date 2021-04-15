from homeassistant import config_entries
from homeassistant.components.mqtt import valid_subscribe_topic
from .const import DOMAIN, CONF_OPENWB_BASE_TOPIC, DEFAULT_BASE_TOPIC
import voluptuous as vol


class OpenWbConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow."""

    VERSION = 1

    def __init__(self):
        """Initialize flow."""
        self._basetopic = DEFAULT_BASE_TOPIC

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        if self.show_advanced_options:
            return await self.async_step_config()
        return await self.async_step_confirm()

    async def async_step_config(self, user_input=None):
        """Confirm the setup."""
        errors = {}
        data = {CONF_OPENWB_BASE_TOPIC: self._basetopic}

        if user_input is not None:
            bad_basetopic = False
            basetopic = user_input[CONF_OPENWB_BASE_TOPIC]
            if basetopic.endswith("/#"):
                basetopic = basetopic[:-2]
            try:
                valid_subscribe_topic(f"{basetopic}/#")
            except vol.Invalid:
                errors["base"] = "invalid_discovery_topic"
                bad_basetopic = True
            else:
                data[CONF_OPENWB_BASE_TOPIC] = basetopic
            if not bad_basetopic:
                return self.async_create_entry(title="OpenWB", data=data)

        fields = {}
        fields[vol.Optional(CONF_OPENWB_BASE_TOPIC, default=self._basetopic)] = str

        return self.async_show_form(
            step_id="config", data_schema=vol.Schema(fields), errors=errors
        )

    async def async_step_confirm(self, user_input=None):
        """Confirm the setup."""

        data = {CONF_OPENWB_BASE_TOPIC: self._basetopic}

        if user_input is not None:
            return self.async_create_entry(title="OpenWB", data=data)

        return self.async_show_form(step_id="confirm")