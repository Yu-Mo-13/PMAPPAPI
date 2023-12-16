import configparser

def get_config(section, key):
    config = configparser.SafeConfigParser()
    config.read('const.ini')
    return config.get(section, key)