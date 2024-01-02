import rtyaml as yaml


def get_settings():
    with open(r'./settings.yml') as settingsFile:
        settings = yaml.load(settingsFile)
        return settings


def save_settings(settings):
    try:
        with open(r'./settings.yml', 'w') as settingsFile:
            yaml.dump(settings, settingsFile)
            return True
    except:
        print("A problem occurred while attempting to save the settings file.")
        return False
