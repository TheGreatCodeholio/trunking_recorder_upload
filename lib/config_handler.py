import json
import logging

module_logger = logging.getLogger('icad_tr_uploader.config')

default_config = {
    "log_level": 1,
}


def generate_default_config():
    try:

        global default_config
        default_data = default_config.copy()

        return default_data

    except Exception as e:
        module_logger.error(f'Error generating default configuration: {e}')
        return None


def load_config_file(file_path):
    """
    Loads the configuration file and encryption key.
    """

    # Attempt to load the configuration file
    try:
        with open(file_path, 'r') as f:
            config_data = json.load(f)
    except FileNotFoundError:
        # Config not found, create and load.
        module_logger.warning(f'Configuration file {file_path} not found. Creating default.')
        config_data = generate_default_config()
        if config_data:
            save_config_file(file_path, config_data)
            module_logger.warning(f'Created Default Configuration.')
            return config_data
    except json.JSONDecodeError:
        module_logger.error(f'Configuration file {file_path} is not in valid JSON format.')
        return None
    except Exception as e:
        module_logger.error(f'Unexpected Exception Loading file {file_path} - {e}')
        return None

    return config_data


def save_config_file(file_path, default_data):
    """Creates a configuration file with default data if it doesn't exist."""
    try:
        with open(file_path, "w") as outfile:
            outfile.write(json.dumps(default_data, indent=4))
        return True
    except Exception as e:
        module_logger.error(f'Unexpected Exception Saving file {file_path} - {e}')
        return None


def get_talkgroup_config(talkgroup_config, call_data):
    talkgroup_dec = call_data.get("talkgroup", 0)
    talkgroup_config_data = {}  # Initialize as an empty dict

    # Determine the appropriate talkgroup configuration
    if talkgroup_dec > 0 and talkgroup_config:
        talkgroup_dec_str = str(talkgroup_dec)
        talkgroup_config_data = talkgroup_config.get(talkgroup_dec_str) or talkgroup_config.get("*", {})

    return talkgroup_config_data
