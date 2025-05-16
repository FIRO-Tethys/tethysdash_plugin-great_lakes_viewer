from intake.source import base
import os
import json


class Map(base.DataSource):
    container = "python"
    version = "0.0.1"
    name = "great_lakes_map"
    visualization_args = {}
    visualization_group = "Great Lakes Viewer"
    visualization_label = "Great Lakes Viewer Map"
    visualization_type = "map"
    _user_parameters = []

    def __init__(self, metadata=None, **kwargs):
        super(Map, self).__init__(metadata=metadata)

    def read(self):
        module_path = os.path.dirname(__file__)
        file_path = f'{module_path}/data/geojson/map_layers.json'
        layers_config = {}
        with open(file_path) as file:
            layers_config = json.load(file)
        layers = layers_config['args_string']['layers']
        return {
            "baseMap": "https://server.arcgisonline.com/arcgis/rest/services/World_Topo_Map/MapServer",
            "layers": layers,
            "layerControl": True,
            "viewConfig": {
                "center": [-9420639.46478766, 5668078.400971366],
                "zoom": 6.168853136274057
            },
        }
