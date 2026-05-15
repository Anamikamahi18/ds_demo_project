import yaml
from os.path import join

CONFIG_PATH = "config"
config_name = "config.yaml"


def load_config(config_name=config_name):
    with open(join(CONFIG_PATH, config_name), "r") as f:
        config = yaml.safe_load(f)
    return config
