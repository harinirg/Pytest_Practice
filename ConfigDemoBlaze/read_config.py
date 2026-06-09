from configparser import ConfigParser

def get_config(category,key):
    config=ConfigParser()
    config.read("ConfigDemoBlaze\config.ini")
    return config.get(category,key)