import configparser

path = './data/chap14_config.ini'


def create_config():
    """
    Create a configuration file
    """
    config = configparser.ConfigParser()
    section = 'Settings'
    config.add_section(section)
    config.set(section, 'font', 'Courier')
    config.set(section, 'font_size', '10')
    config.set(section, 'font_style', 'normal')
    # Interpolation
    config.set(section, 'font_info', "You are using %(font)s at %(font_size)s pt")

    with open(path, 'w') as config_file:
        config.write(config_file)

create_config()


def read_config():
    config = configparser.ConfigParser()
    config.read(path)
    print(config.get('Settings', 'font'))
    print(config.get('Settings', 'font_size'))
    print(config.get('Settings', 'font_style'))
    print(config.get('Settings', 'font_info'))

read_config()


def update_config():
    config = configparser.ConfigParser()
    config.read(path)
    section = 'Settings'
    config.set(section, 'font', 'Consolas')
    config.set(section, 'font_size', '16')
    config.set(section, 'font_style', 'bold')

    with open(path, 'w') as config_file:
        config.write(config_file)

update_config()
read_config()


def delete_config():
    config = configparser.ConfigParser()
    config.read(path)
    config.remove_option('Settings', 'font_style')

    with open(path, 'w') as config_file:
        config.write(config_file)

delete_config()
try:
    read_config()
except Exception as e:
    print(str(e))
