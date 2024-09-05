import os
import json

from util.system_path import get_cnas_path

class config:
    """
    Load and Save CNAS config

    >>> from util.config import config
    >>> c = config(False)
    >>> c.set("test", "1234")
    >>> c.get("test")
    '1234'
    >>> c.save()
    >>> c.load()  # doctest: +SKIP
    >>> c.get("test")
    '1234'

    """

    def __init__(self, early_load=True):
        self.config_path = get_cnas_path()
        self.config_file = os.path.join(self.config_path, "config.json")
        self.config_data = {}

        # create folder and file
        file_exist = os.path.exists(self.config_file)
        if not file_exist:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                f.write('')
        if early_load and file_exist:
            self.load()

    def load(self):
        if not os.path.exists(self.config_file):
            assert False, "no config file"
        try:
            with open(self.config_file, encoding='utf-8') as f:
                self.config_data = json.load(f)
        except Exception as e:
            print("config error :" + e)

    def save(self):
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config_data, f, indent=4)

    def get(self, key):
        return self.config_data.get(key)

    def set(self, key, value):
        self.config_data[key] = value


CONFIG = config()
