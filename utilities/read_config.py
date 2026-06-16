import configparser
import os

class ReadConfig:
    config_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "config_files",
        "config.ini"
    )

    @staticmethod
    def get_config_value(section_name, key_name):
        config = configparser.ConfigParser()
        config.read(ReadConfig.config_path)
        return config.get(section_name, key_name)
