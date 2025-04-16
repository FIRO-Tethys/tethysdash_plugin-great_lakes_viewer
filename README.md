# TethysDash Plugin: Great Lakes Viewer

![Demo](/images/demo.png)

## Install the plugin

1. Clone the repo: `git clone https://github.com/FIRO-Tethys/tethysdash_plugin-great_lakes_viewer.git`

2. Enter the folder and install the plugin:
   ```
   cs tethysdash_plugin-great_lakes_viewer
   python setup.py develop
   ```

3. Now the plugin will show up under the `Visualization Type`:

    ![Demo](/images/plugin.png)

## Make a dashboard

1. Create a new dashboard

2. Add a map plugin:
   - Choose a base map
   - Add a GeoJSON layer, using `GreatLakes.geojson` as Source, `style.json` as Style. These files are under the `visualizations/data/geojson` folder.
   - Under the `Attributes/Popup` tab, set `Variable Input Name` of `label` as `Lake`

3. Add a plot plugin:
    - Under `Visualization Type`, choose `Great Lakes Viewer Plots`
    - Set `Lake` as `${Lake}`, which is defined in the step 2
    
    ![Demo](/images/plot.png)

4. Click the lake on the map, the plot will change accordingly