import argparse
import os
import time

from lib.audio_file_handler import load_call_json
from lib.call_processor import process_tr_call
from lib.config_handler import load_config_file
from lib.logging_handler import CustomLogger

app_name = "trunk_recorder_upload"
__version__ = "1.0"

root_path = os.getcwd()
config_file_name = "config.json"

log_file_name = f"{app_name}.log"

log_path = os.path.join(root_path, 'log')

if not os.path.exists(log_path):
    os.makedirs(log_path)

config_path = os.path.join(root_path, 'etc')

logging_instance = CustomLogger(1, f'{app_name}',
                                os.path.join(log_path, log_file_name))

try:
    config_data = load_config_file(os.path.join(config_path, config_file_name))
    logging_instance.set_log_level(config_data["log_level"])
    logger = logging_instance.logger
    logger.info("Loaded Config File")
except Exception as e:
    print(f'Error while <<loading>> configuration : {e}')
    time.sleep(5)
    exit(1)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Process Arguments.')
    parser.add_argument("-s", "--system_short_name", type=str, help="System Short Name.")
    parser.add_argument("-a", "--audio_path", type=str, help="Path to WAV.")
    args = parser.parse_args()
    return args


def main():
    logger.info("Starting Trunking Recorder Upload")
    args = parse_arguments()

    audio_path = args.audio_path.replace(".wav", ".mp3")

    call_data = load_call_json(audio_path.replace(".mp3", ".json"))
    if not call_data:
        exit(1)

    process_tr_call(config_data, args.system_short_name, call_data, audio_path)

if __name__ == '__main__':
    main()