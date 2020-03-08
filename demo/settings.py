import yaml
from pathlib import Path


def load_config(conf_file=None):
    default_file = Path(__file__).parent / 'config.yaml'
    with open(default_file) as f:
        config = yaml.safe_load(f)
    config_dict = {}
    if conf_file:
        config_dict = yaml.safe_load(conf_file)
        config.update(**config_dict)
    return config
