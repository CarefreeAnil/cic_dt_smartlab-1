import json
import os

CONFIG = {    
    'realtime_db_path': './sensor_data_realtime.db',
    'history_db_path': './sensor_data_history.db'
}

# Get the directory of the current running Python file
local_repository = os.path.dirname(os.path.abspath(__file__))

CONFIG["TOPIC_FILE_PATH"]= f"{local_repository}/shared_topic.json"
CONFIG["ifc_file"] = f"{local_repository}/local_files/smartLab.ifc"
CONFIG["mqtt_csv"] = f"{local_repository}/local_files/Topic_Ifc_Mapping.csv"
local_config = f"{local_repository}/local_files/smartlab_config.json"

with open(local_config, "r") as f:
    data = json.load(f)
    CONFIG.update(data)

def load_link():
    local_repository = os.path.dirname(os.path.abspath(__file__))
    topic_ifc_link = f"{local_repository}/local_files/topic_ifc_link.json"

    with open(topic_ifc_link, "r") as f:
        link = json.load(f)
    return link

sensor_ifc_link = load_link()

mqtt_topics = list(sensor_ifc_link.keys())
CONFIG['mqtt_topics'] = mqtt_topics 

# Constants for thresholds
THRESHOLDS = CONFIG["thresholds"]

GROUPS_AND_TOPICS = {}
for k in CONFIG["group_keys"]:
    GROUPS_AND_TOPICS[k] = list(filter(lambda s: k.lower() in s.lower(), mqtt_topics))

if __name__ == "__main__":
    from pprint import pprint
    pprint(CONFIG)