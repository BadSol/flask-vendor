import json
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, 'vendor/SECRETS.json')) as data_file:
    secrets = json.load(data_file)
