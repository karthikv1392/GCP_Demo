_Author_ = "********"

# Initalizing all basic configurations

from configparser import ConfigParser
import traceback

CONFIG_FILE = "settings.conf"
CONFIG_SECTION = "settings"

class Initialize():
    def __init__(self):
        data_path = ""
        energy_val = 19160.0  # starting energy value as per CupCarbon
        component_count = 0  # The total number of sensors for which the monitoring needs to be done
        data_file = ""
        json_path = ""
        port = 8067 # Default port
        try:
            parser = ConfigParser()
            parser.read(CONFIG_FILE)
            self.request_url = parser.get(CONFIG_SECTION, "request_url")
            self.api_key = parser.get(CONFIG_SECTION, "api_key")
            self.port = int(parser.get(CONFIG_SECTION, "port"))
            self.upload_path = parser.get(CONFIG_SECTION, "upload_path")


        except Exception as e:
            traceback.print_exc()


