import json
import logging

module_logger = logging.getLogger('trunk_recorder_upload.audio_file_handler')


def load_call_json(json_file_path):
    try:
        with open(json_file_path, 'r') as f:
            call_data = json.load(f)
        module_logger.info(f"Loaded <<Call>> <<Metadata>> Successfully")
        return call_data
    except FileNotFoundError:
        # Call Metadata JSON not found.
        module_logger.warning(f'<<Call>> <<Metadata>> file {json_file_path} not found.')
        return None
    except json.JSONDecodeError:
        module_logger.error(f'<<Call>> <<Metadata>> file {json_file_path} is not in valid JSON format.')
        return None
    except Exception as e:
        module_logger.error(f"Unexpected <<Error>> while loading <<Call>> <<Metadata>> {json_file_path}: {e}")
        return None

