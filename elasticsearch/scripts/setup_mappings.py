"""
  This script is used as a bootstraper of Elasticsearch component 
  templates, index templates and index patterns for ingestion by
  Logstash.

  Author: Kevin C-Dubois (kcdubois@outlook.com)
"""

import json
import logging
from pathlib import Path

import elasticsearch


ROOT_DIR = Path('.').parent
MAPPINGS_DIR = Path.joinpath(ROOT_DIR, "mappings")
LOGGER = logging.getLogger(__name__)


def _load_components():
  """ Load components files from ./mappings """
  components = []

  for file in MAPPINGS_DIR.iterdir():
    if file.suffix == "json":
      with open(file) as jsonfile:
        components.append(json.load(file))
    
  return components


def run():
  """ Default handler when script is run """
  components = _load_components()



if __name__ == "__main__":
  run()
