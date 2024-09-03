import os
import json


class config:
    """
    Load and Save CNAS config

    >>> from util.config import config
    >>> c = config()
    >>> c.set("test", "1234")
    >>> c.get("test")
    '1234'
    >>> c.save()
    >>> c.load()
    >>> c.get("test")
    '1234'

    """

    def __init__(self, early_load=True):
        home_path = os.path.expanduser('~')
        self.config_path = os.path.join(home_path, ".cnas")
        self.config_file = os.path.join(self.config_path, "config.json")
        self.config_data = {}

        # create folder and file
        os.makedirs(self.config_path, exist_ok=True)
        if not os.path.exists(self.config_file):
            with open(self.config_file, 'w', encoding='utf-8') as f:
                f.write('')
        if early_load:
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

