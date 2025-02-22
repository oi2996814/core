"""Const for iOS."""

DOMAIN = "ios"

ATTR_BATTERY = "battery"
ATTR_BATTERY_LEVEL = "level"
ATTR_BATTERY_STATE = "state"
ATTR_BATTERY_STATE_UNPLUGGED = "Not Charging"
ATTR_BATTERY_STATE_CHARGING = "Charging"
ATTR_BATTERY_STATE_FULL = "Full"
ATTR_BATTERY_STATE_UNKNOWN = "Unknown"

BATTERY_STATES = [
    ATTR_BATTERY_STATE_UNPLUGGED,
    ATTR_BATTERY_STATE_CHARGING,
    ATTR_BATTERY_STATE_FULL,
    ATTR_BATTERY_STATE_UNKNOWN,
]

ATTR_DEVICE = "device"
ATTR_DEVICE_ID = "deviceId"
ATTR_DEVICE_NAME = "name"
ATTR_DEVICE_PERMANENT_ID = "permanentID"
ATTR_DEVICE_SYSTEM_VERSION = "systemVersion"
ATTR_DEVICE_TYPE = "type"

CONF_ACTION_NAME = "name"
CONF_ACTION_BACKGROUND_COLOR = "background_color"
CONF_ACTION_LABEL = "label"
CONF_ACTION_LABEL_COLOR = "color"
CONF_ACTION_LABEL_TEXT = "text"
CONF_ACTION_ICON = "icon"
CONF_ACTION_ICON_COLOR = "color"
CONF_ACTION_ICON_ICON = "icon"
CONF_ACTIONS = "actions"
CONF_ACTION_SHOW_IN_CARPLAY = "show_in_carplay"
CONF_ACTION_SHOW_IN_WATCH = "show_in_watch"
CONF_ACTION_USE_CUSTOM_COLORS = "use_custom_colors"
