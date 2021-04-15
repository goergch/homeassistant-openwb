DOMAIN = "openwb"
CONF_OPENWB_BASE_TOPIC = "openwb_topic"
DEFAULT_BASE_TOPIC = "openWB"

from homeassistant.const import (
    POWER_WATT,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_VOLTAGE,
    DEVICE_CLASS_POWER_FACTOR,
    VOLT,
    ELECTRICAL_CURRENT_AMPERE,
    ENERGY_KILO_WATT_HOUR,
    DEVICE_CLASS_ENERGY,
    LENGTH_METERS,
    TIME_MINUTES,
)

CHARGE_MODES = {"immediate": 0, "min+pv": 1, "pv": 2, "stop": 3, "standby": 4}

SENSOR_DEFINITIONS = {
    "/global/ChargeMode": {
        "name": "Charge Mode",
        "entity_id": "charge_mode",
        "enable_default": True,
    },
    "/global/WAllChargePoints": {
        "name": "Power all charge point",
        "entity_id": "power",
        "enable_default": True,
        "device_class": DEVICE_CLASS_POWER,
        "unit": POWER_WATT,
    },
    "/global/strLastmanagementActive": {
        "name": "Lastmanagement active",
        "entity_id": "lastmanagement",
        "enable_default": True,
    },
    "/lp/1/TimeRemainin": {
        "name": "Charge point 1 Remaining Time for Charge",
        "entity_id": "lp_1_time_remaining",
        "enable_default": True,
        "unit": TIME_MINUTES,
    },
    "/lp/1/%Soc": {
        "name": "Charge point 1 state of charge",
        "entity_id": "lp_1_soc",
        "enable_default": True,
    },
    "/lp/1/kWhDailyCharged": {
        "name": "Charge point 1 daily charged energy",
        "entity_id": "lp_1_daily_charged",
        "enable_default": True,
        "device_class": DEVICE_CLASS_ENERGY,
        "unit": ENERGY_KILO_WATT_HOUR,
    },
    "/lp/1/strChargePointName": {
        "name": "Charge point 1 name",
        "entity_id": "lp_1_name",
        "enable_default": True,
    },
    "/lp/1/W": {
        "name": "Charge point 1 power",
        "entity_id": "lp_1_power",
        "enable_default": True,
        "device_class": DEVICE_CLASS_POWER,
        "unit": POWER_WATT,
    },
    "/lp/1/VPhase1": {
        "name": "Charge point 1 voltage Phase 1",
        "entity_id": "lp_1_v_phase1",
        "enable_default": True,
        "device_class": DEVICE_CLASS_VOLTAGE,
        "unit": VOLT,
    },
    "/lp/1/VPhase2": {
        "name": "Charge point 1 voltage Phase 2",
        "entity_id": "lp_1_v_phase2",
        "enable_default": True,
        "device_class": DEVICE_CLASS_VOLTAGE,
        "unit": VOLT,
    },
    "/lp/1/VPhase3": {
        "name": "Charge point 1 voltage Phase 3",
        "entity_id": "lp_1_v_phase3",
        "enable_default": True,
        "device_class": DEVICE_CLASS_VOLTAGE,
        "unit": VOLT,
    },
    "/lp/1/kmCharged": {
        "name": "Charge point 1 km charged",
        "entity_id": "lp_1_km_charged",
        "enable_default": True,
        "unit": LENGTH_METERS,
    },
    "/lp/1/energyConsumptionPer100km": {
        "name": "Charge point 1 Comsumption per 100km",
        "entity_id": "lp_1_consumption",
        "enable_default": True,
    },
    "/lp/1/kWhCounter": {
        "name": "Charge point 1 Comsumption per 100km",
        "entity_id": "lp_1_kwh_counter",
        "enable_default": True,
        "device_class": DEVICE_CLASS_ENERGY,
        "unit": ENERGY_KILO_WATT_HOUR,
    },
    "/lp/1/countPhasesInUse": {
        "name": "Charge point 1 count phases in use",
        "entity_id": "lp_1_phases_in_use",
        "enable_default": True,
    },
    "/lp/1/kWhActualCharged": {
        "name": "Charge point 1 actual charged",
        "entity_id": "lp_1_kwh_actual_charged",
        "enable_default": True,
        "device_class": DEVICE_CLASS_ENERGY,
        "unit": ENERGY_KILO_WATT_HOUR,
    },
    "/lp/1/ChargeStatus": {
        "name": "Charge point 1 charge status",
        "entity_id": "lp_1_kwh_charge_status",
        "enable_default": True,
    },
    "/lp/1/kWhChargedSincePlugged": {
        "name": "Charge point 1 charged since plugged",
        "entity_id": "lp_1_kwh_since_plugged",
        "enable_default": True,
        "device_class": DEVICE_CLASS_ENERGY,
        "unit": ENERGY_KILO_WATT_HOUR,
    },
    "/lp/1/PfPhase1": {
        "name": "Charge point 1 power factor phase 1",
        "entity_id": "lp_1_pf_phase1",
        "enable_default": True,
        "device_class": DEVICE_CLASS_POWER_FACTOR,
    },
    "/lp/1/PfPhase2": {
        "name": "Charge point 1 power factor phase 2",
        "entity_id": "lp_1_pf_phase2",
        "enable_default": True,
        "device_class": DEVICE_CLASS_POWER_FACTOR,
    },
    "/lp/1/PfPhase3": {
        "name": "Charge point 1 power factor phase 3",
        "entity_id": "lp_1_pf_phase3",
        "enable_default": True,
        "device_class": DEVICE_CLASS_POWER_FACTOR,
    },
    "/lp/1/APhase1": {
        "name": "Charge point 1 current Phase 1",
        "entity_id": "lp_1_a_phase1",
        "enable_default": True,
        "device_class": DEVICE_CLASS_CURRENT,
        "unit": ELECTRICAL_CURRENT_AMPERE,
    },
    "/lp/1/APhase2": {
        "name": "Charge point 1 current Phase 2",
        "entity_id": "lp_1_a_phase2",
        "enable_default": True,
        "device_class": DEVICE_CLASS_CURRENT,
        "unit": ELECTRICAL_CURRENT_AMPERE,
    },
    "/lp/1/APhase3": {
        "name": "Charge point 1 current Phase 3",
        "entity_id": "lp_1_a_phase3",
        "enable_default": True,
        "device_class": DEVICE_CLASS_CURRENT,
        "unit": ELECTRICAL_CURRENT_AMPERE,
    },
    "/lp/1/lastRfId": {
        "name": "Charge point 1 last RFID",
        "entity_id": "lp_1_last_rfid",
        "enable_default": True,
    },
}
BINARY_SENSOR_DEFINITIONS = {
    "/lp/1/boolChargePointConfigured": {
        "name": "Charge point 1 configured",
        "entity_id": "lp_1_configured",
        "enable_default": True,
    },
    "/lp/1/boolChargeAtNight ": {
        "name": "Charge point 1 charge at night",
        "entity_id": "lp_1_charge_at_night",
        "enable_default": True,
    },
    "/lp/1/boolDirectModeChargekWh ": {
        "name": "Charge point 1 direct mode kWh",
        "entity_id": "lp_1_direct_mode_kwh",
        "enable_default": True,
    },
    "/lp/1/boolDirectModeChargeSoC": {
        "name": "Charge point 1 direct mode SoC",
        "entity_id": "lp_1_direct_mode_soc",
        "enable_default": True,
    },
    "/lp/1/boolFinishAtTimeChargeActive": {
        "name": "Charge point 1 direct mode SoC",
        "entity_id": "lp_1_finish_at_time_active",
        "enable_default": True,
    },
    "/lp/1/AutolockConfigured": {
        "name": "Charge point 1 autolock configured",
        "entity_id": "lp_1_autolock_configured",
        "enable_default": True,
    },
    "/lp/1/boolPlugStat": {
        "name": "Charge point 1 Plug state",
        "entity_id": "lp_1_plug_state",
        "enable_default": True,
    },
    "/lp/1/ChargePointEnabled": {
        "name": "Charge point 1 enabled",
        "entity_id": "lp_1_enabled",
        "enable_default": True,
    },
    "/lp/1/boolChargeStat": {
        "name": "Charge point 1 charge state",
        "entity_id": "lp_1_charge_state",
        "enable_default": True,
    },
    "/boolChargeAtNight_direct": {
        "name": "Charge at Night Direct Mode",
        "entity_id": "chargeatnight_direct",
        "enable_default": True,
    },
    "/boolChargeAtNight_nurpv": {
        "name": "Charge at Night Direct only PV",
        "entity_id": "chargeatnight_onlypv",
        "enable_default": True,
    },
    "/boolChargeAtNight_minpv": {
        "name": "Charge at Night Direct min PV",
        "entity_id": "chargeatnight_minpv",
        "enable_default": True,
    },
}