from intake.source import base
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import os


class Plots(base.DataSource):
    container = "python"
    version = "0.0.1"
    name = "great_lakes_plots"
    visualization_args = {
        "lake": [
            {"value": "lake erie", "label": "Lake Erie"},
            {"value": "lake ontario", "label": "Lake Ontario"},
            {"value": "lake superior", "label": "Lake Superior"},
            {"value": "lake michigan-huron", "label": "Lake Michigan-Huron"},
            {"value": "lake st. clair", "label": "Lake St. Clair"}
        ]
    }
    visualization_group = "Great Lakes Viewer"
    visualization_label = "Great Lakes Viewer Plots"
    visualization_type = "plotly"
    _user_parameters = []

    def __init__(self, lake, metadata=None):
        self.lake = lake
        super(Plots, self).__init__(metadata=metadata)

    def read(self):
        module_path = os.path.dirname(__file__)
        lake = self.lake.title()
        file_path = f'{module_path}/data/{lake}.csv'
        df = pd.read_csv(file_path)

        plot = go.Figure()
        plot.add_trace(go.Scatter(
            x=df['Month'].to_list(),
            y=df.iloc[:, 1].to_list(),
            mode='lines',
            line=dict(width=2, color='blue')
        ))
        plot.update_layout(
            title=f'{lake} Water Levels',
            xaxis=dict(title='Year'),
            yaxis=dict(title='Water Level (meters)', range=[0, None]),
        )

        data = []
        for trace in plot.data:
            trace_json = trace.to_plotly_json()
            if 'x' in trace_json and isinstance(trace_json['x'], np.ndarray):
                trace_json['x'] = trace_json['x'].tolist()
            if 'y' in trace_json and isinstance(trace_json['y'], np.ndarray):
                trace_json['y'] = trace_json['y'].tolist()
            data.append(trace_json)
        layout = plot.to_plotly_json()["layout"]
        config = {'autosizable': True, 'responsive': True}
        return {
            "data": data,
            "layout": layout,
            "config": config
        }
