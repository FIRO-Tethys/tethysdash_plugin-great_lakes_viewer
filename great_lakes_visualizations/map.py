from intake.source import base
import os
import json


class Map(base.DataSource):
    container = "python"
    version = "0.0.1"
    name = "great_lakes_map"
    visualization_description = ("Map for Great Lakes")
    visualization_tags = ["map", "great lakes"]
    visualization_args = {}
    visualization_group = "Great Lakes Viewer"
    visualization_label = "Great Lakes Viewer Map"
    visualization_type = "map"
    visualization_attribution = "USGS"
    _user_parameters = []

    def __init__(self, metadata=None, **kwargs):
        super(Map, self).__init__(metadata=metadata)

    def read(self):
        module_path = os.path.dirname(__file__)
        file_path = f'{module_path}/data/geojson/map_layers.json'
        map_config = {}
        with open(file_path) as file:
            map_config = json.load(file)
        return map_config['args_string']
