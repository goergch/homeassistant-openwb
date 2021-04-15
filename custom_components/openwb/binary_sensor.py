from .const import BINARY_SENSOR_DEFINITIONS, DEFAULT_BASE_TOPIC, DOMAIN

from homeassistant.components import mqtt
from homeassistant.core import callback
from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.util import slugify
import logging

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, entry, async_add_entities):

    sensors = []

    for topic in BINARY_SENSOR_DEFINITIONS:
        sensors.append(OpenWBBinarySensor(topic))

    async_add_entities(sensors)


class OpenWBBinarySensor(BinarySensorEntity):
    def __init__(self, topic):
        self._definition = BINARY_SENSOR_DEFINITIONS[topic]
        self._entity_id = DOMAIN + "_" + self._definition.get("entity_id")
        self._topic = DEFAULT_BASE_TOPIC + topic
        self._name = self._definition.get("name")
        self._enable_default = self._definition.get("enable_default")
        self._icon = self._definition.get("icon")
        self._device_class = self._definition.get("device_class")
        self._state = None

    async def async_added_to_hass(self):
        """Subscribe to MQTT events."""

        @callback
        def message_received(message):
            """Handle new MQTT messages."""
            if message.payload == "0":
                self._state = False
            elif message.payload == "1":
                self._state = True
            else:
                self._state = None

            self.async_write_ha_state()

        _LOGGER.info("openWB topic: " + self._topic)
        await mqtt.async_subscribe(self.hass, self._topic, message_received, 1)

    @property
    def name(self):
        """Return the name of the sensor supplied in constructor."""
        return self._name

    @property
    def entity_id(self):
        """Return the entity ID for this sensor."""
        return f"sensor.{self._entity_id}"

    @property
    def state(self):
        """Return the current state of the entity."""
        return self._state

    @property
    def device_class(self):
        """Return the device_class of this sensor."""
        return self._device_class

    @property
    def entity_registry_enabled_default(self) -> bool:
        """Return if the entity should be enabled when first added to the entity registry."""
        return self._enable_default

    @property
    def icon(self):
        """Return the icon of this sensor."""
        return self._icon
