import os
import yaml

DIRECTORY = os.path.abspath(os.path.dirname(__file__))
FILENAME = "kaomojis.yml"
FILEPATH = os.path.join(DIRECTORY, FILENAME)

def load_kaomojis(filepath=FILEPATH):
    _f = open(filepath, "r+",encoding='utf-8')
    return yaml.load(_f)