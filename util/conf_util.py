import yaml


def read_config(config_path):
    with open(config_path, "r", encoding="utf-8") as f_config:
        config_data = yaml.load(f_config.read())
    return config_data

def get_default_config():
    default_path = "./config.yaml"
    return read_config(default_path)